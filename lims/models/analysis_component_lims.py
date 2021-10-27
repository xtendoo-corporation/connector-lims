# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AnalysisComponentLims(models.Model):
    _name = "analysis.component.lims"
    _description = "Analysis Component LIMS"
    analysis_ids = fields.Many2one(
        "analysis.lims",
        "Analysis lims",
        invisible=True,
    )
    parameter = fields.Char(string="Parameter", store=True)
    comparator = fields.Selection(
        [
            (">", "Greater than"),
            (">=", "Greater than or equal"),
            ("<", "Smaller than"),
            ("<=", "Smaller than or equal"),
            ("=", "equal"),
        ],
        "Comparator",
    )
    min_value = fields.Float(string="Min Value", store=True)
    max_value = fields.Float(string="Max Value", store=True)
