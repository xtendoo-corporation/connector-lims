# Copyright 2021 - Manuel Calero <https://xtendoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class StockMove(models.Model):
    _inherit = "stock.move"

    analysis_ids = fields.One2many(
        "analysis.line.lims",
        "stock_move_id",
        invisible=True,
    )

    is_product_sample = fields.Boolean(
        "Is Product Sample",
        compute="_compute_is_product_sample",
        Stote=True,
        readonly="1",
    )

    def _compute_is_product_sample(self):
        self.is_product_sample = self.product_id.is_product_sample

    def create_new_analysis(self):
        move_line = self._get_stock_move_line()
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "lims.analysis_new_action"
        )
        action["context"] = {
            "stock_move_id": self.id,
            "lot_id": move_line.lot_id.id,
            "customer_id": self.picking_id.partner_id.id,
            "product_id": move_line.product_id.product_tmpl_id.id,
        }
        return action

    def _get_stock_move_line(self):
        return self.env["stock.move.line"].search([("move_id", "=", self.id)])
