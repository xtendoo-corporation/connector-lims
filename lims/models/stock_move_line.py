# Copyright 2021 - Manuel Calero <https://xtendoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    analysis_ids = fields.One2many(
        "analysis.line.lims",
        "stock_move_line_id",
        invisible=True,
    )
