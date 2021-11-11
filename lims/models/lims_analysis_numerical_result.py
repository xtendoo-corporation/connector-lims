# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LimsAnalysisNumericalResult(models.Model):
    _name = "lims.analysis.numerical.result"
    _description = "LIMS Analysis Numerical Result"

    analysis_ids = fields.Many2one(
        "lims.analysis.line",
        "Analysis lims Line",
    )
    component_ids = fields.Many2one(
        "lims.analysis.component",
        "Analysis lims Component",
    )
    value = fields.Float(string="Value", store=True)

    component_uom = fields.Many2one(related="component_ids.component_uom", store=True)
    limit_value = fields.Float(string="Limit Value", store=True)
    between_limit_value = fields.Char(string="Between Limit Value", store=True)
    is_null = fields.Boolean(string="Is Null", store=True)
    corrected_value = fields.Float(string="Corrected Value", store=True)
    loq = fields.Float(string="LOQ", store=True)
    corrected_loq = fields.Float(string="Corrected LOQ", store=True)
    dil_fact = fields.Float(string="Dil. Fact.", store=True)
    reason = fields.Char(string="Reason", store=True)
    comment = fields.Char(string="Comment", store=True)
