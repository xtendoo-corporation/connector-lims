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
    is_product_sample = fields.Boolean(
        "Is Product Sample",
        related="product_id.is_product_sample",
        store=True,
        readonly="1",
    )

    def create_new_analysis(self):
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "lims.analysis_new_action"
        )
        action["context"] = {
            "stock_move_line_id": self.id,
            "lot_id": self.lot_id.id,
            "customer_id": self.picking_id.partner_id.id,
            "product_id": self.product_id.product_tmpl_id.id,
        }
        return action
