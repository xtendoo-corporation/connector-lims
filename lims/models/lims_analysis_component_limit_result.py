# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LimsAnalysisComponentLimitResult(models.Model):
    _name = "lims.analysis.component.limit.result"
    _description = "Component LIMS Limit Result"

    component_ids = fields.Many2one(
        "lims.analysis.component",
        "Analysis lims Component",
    )
    operator_from = fields.Selection(
        [
            (">", ">"),
            (">=", ">="),
            ("<", "<"),
            ("<=", "<="),
            ("=", "="),
        ],
        "Operator From",
    )
    limit_value_from = fields.Float(string="Limit Value From", store=True)
    operator_to = fields.Selection(
        [
            (">", ">"),
            (">=", ">="),
            ("<", "<"),
            ("<=", "<="),
            ("=", "="),
        ],
        "Operator From",
    )
    limit_value_to = fields.Float(string="Limit Value From", store=True)
    type = fields.Char(string="Type", store=True)
    state = fields.Selection(
        [
            ("conform", "Conform"),
            ("warning", "Warning"),
            ("not_conform", "Not Conform"),
        ],
        "State",
    )
    message = fields.Char(string="Message", store=True)
