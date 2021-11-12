# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LimsAnalysisParameterLimitResult(models.Model):
    _name = "lims.analysis.parameter.limit.result"
    _description = "parameter LIMS Limit Result"

    parameter_ids = fields.Many2one(
        "lims.analysis.parameter",
        "Analysis lims parameter",
    )
    operator_from = fields.Selection(
        [
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
            ("=", "="),
        ],
        "Operator to",
    )
    limit_value_to = fields.Float(string="Limit Value to", store=True)
    type = fields.Selection(
        [
            ("LIMIT", "LIMIT"),
            ("BETWEEN", "BETWEEN"),
        ],
        "Type",
        store=True,
    )
    state = fields.Selection(
        [
            ("conform", "Conform"),
            ("warning", "Warning"),
            ("not_conform", "Not Conform"),
        ],
        "State",
    )
    message = fields.Char(string="Message", store=True)
