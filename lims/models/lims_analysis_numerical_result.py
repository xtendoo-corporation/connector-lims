# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class LimsAnalysisNumericalResult(models.Model):
    _name = "lims.analysis.numerical.result"
    _description = "LIMS Analysis Numerical Result"

    analysis_ids = fields.Many2one(
        "lims.analysis.line",
        "Analysis lims Line",
    )
    parameter_ids = fields.Many2one(
        "lims.analysis.parameter",
        "Analysis lims parameter",
    )
    value = fields.Float(string="Value", store=True, default="")

    parameter_uom = fields.Many2one(related="parameter_ids.parameter_uom", store=True)
    limit_value_char = fields.Char(string="Limit Value", store=True)
    limit_value = fields.Float(string="Limit Value", store=True)
    between_limit_value = fields.Char(string="Between Limit Value", store=True)
    is_null = fields.Boolean(string="Is Null", store=True)
    corrected_value = fields.Float(string="Corrected Value", store=True)
    loq = fields.Float(string="LOQ", store=True)
    corrected_loq = fields.Float(string="Corrected LOQ", store=True)
    dil_fact = fields.Float(string="Dil. Fact.", store=True)
    reason = fields.Char(string="Reason", store=True)
    comment = fields.Char(string="Comment", store=True)
    result = fields.Selection(
        [
            ("none", "Unrealized"),
            ("pass", "Approved"),
            ("fail", "Failed"),
            ("warning", "Warning"),
        ],
        string="Result",
        default="none",
        store=True,
    )

    def _get_value_result(self, value):
        result_value = ""
        result = []
        for parameter in self.parameter_ids:
            result_value = parameter._get_parameter_analysis_result(value)
            if result_value == "warning":
                result_value = "warning"
            if result_value == "not_conform":
                result_value = "fail"
            if result_value == "conform":
                result_value = "pass"
            result.append(result_value)
        return result_value

    @api.onchange("value")
    def _onchange_value(self):
        self.result = self._get_value_result(self.value)
