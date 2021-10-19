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
        action = self.env["ir.actions.act_window"]._for_xml_id(
            "lims.analysis_new_action"
        )
        action["context"] = {
            "stock_move_id": self.id,
        }
        return action
