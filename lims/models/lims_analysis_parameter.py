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
    name = fields.Char(string="Name", store=True)
    parameter_limit_result_ids = fields.One2many(
        "lims.analysis.parameter.limit.result",
        "parameter_ids",
    )
    parameter_uom = fields.Many2one("uom.uom", "Unit of Measure")

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
