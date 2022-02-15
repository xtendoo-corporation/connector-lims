# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LimsAnalysisParameter(models.Model):
    _name = "lims.analysis.parameter"
    _description = "Parameter LIMS"
    # analysis_ids = fields.Many2one(
    #     "lims.analysis",
    #     "Analysis lims",
    # )
    analysis_ids = fields.Many2many(
        "lims.analysis",
        "lims_analysis_lims_analysis_parameter_rel",
        "parameter_id",
        "analysis_id",
        "Analysis lims",
    )
    default_code = fields.Char("Reference", index=True)
    name = fields.Char(string="Name", store=True)
    parameter_limit_result_ids = fields.One2many(
        "lims.analysis.parameter.limit.result",
        "parameter_ids",
    )
    parameter_uom = fields.Many2one("uom.uom", "Unit of Measure")

    _sql_constraints = [
        ("code_uniq", "unique (default_code)", "Code already exists!"),
    ]

    def _get_limit_value_char(self):
        limit_result_char = ""
        for parameter_line in self.parameter_limit_result_ids:
            if parameter_line.type == "LIMIT" and parameter_line.state == "conform":
                if parameter_line.limit_value_from > 0.0:
                    limit_result_char = ("{operator_from} {value_from: .2f}").format(
                        operator_from=parameter_line.operator_from,
                        value_from=parameter_line.limit_value_from,
                    )
                if parameter_line.limit_value_to > 0.0:
                    limit_result_char = ("{operator_to} {value_to: .2f}").format(
                        operator_to=parameter_line.operator_to,
                        value_to=parameter_line.limit_value_to,
                    )
        return limit_result_char

    def _get_limit_value(self):
        limit_result = 0.00
        for parameter_line in self.parameter_limit_result_ids:
            if parameter_line.type == "LIMIT" and parameter_line.state == "conform":
                limit_result = parameter_line.limit_value_to
        return limit_result

    def _get_between_limit_value(self):
        between_limit_result = ""
        for parameter_line in self.parameter_limit_result_ids:
            if parameter_line.type == "BETWEEN" and parameter_line.state == "conform":
                between_limit_result = ("{value_from: .2f} and {value_to: .2f}").format(
                    value_from=parameter_line.limit_value_from,
                    value_to=parameter_line.limit_value_to,
                )
        return between_limit_result

    def _get_parameter_analysis_result(self, value):
        result = "not_conform"
        for parameter_result in self.parameter_limit_result_ids:
            operator_to = ""
            operator_from = ""
            if parameter_result.operator_from:
                if parameter_result.operator_from == "=":
                    operator_from = "=="
                else:
                    operator_from = parameter_result.operator_from
                operator_from = (
                    operator_from + "" + str(parameter_result.limit_value_from)
                )
            if parameter_result.operator_to:
                if parameter_result.operator_to == "=":
                    operator_to = "=="
                else:
                    operator_to = parameter_result.operator_to
                operator_to = operator_to + "" + str(parameter_result.limit_value_to)
            # Es LIMIT
            if parameter_result.type == "LIMIT":
                if operator_to != "":
                    str(value) + "" + operator_to
                if operator_from != "":
                    str(value) + "" + operator_from
            # ES BETWEEN
            else:
                # if eval(str(value) + "" + operator_from) and eval(
                #     str(value) + "" + operator_to
                # ):
                result = parameter_result.state
        return result
