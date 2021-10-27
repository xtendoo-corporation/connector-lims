# Copyright 2021 - Manuel Calero <https://xtendoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"
    analysis_count = fields.Integer(
        "Number of Analysis Generated",
        compute="_compute_analysis_count",
    )

    def _compute_analysis_count(self):
        for order in self:
            order.analysis_count = len(self._get_analysis())

    def _get_analysis(self):
        return self.env["analysis.line.lims"].search(
            [("stock_move_line_id", "in", (self.move_line_nosuggest_ids.ids))]
        )

    def action_view_analysis(self):
        self.ensure_one()
        analysis_line_ids = self._get_analysis().ids
        action = {
            "res_model": "analysis.line.lims",
            "type": "ir.actions.act_window",
        }
        if len(analysis_line_ids) == 1:
            action.update(
                {
                    "view_mode": "form",
                    "res_id": analysis_line_ids[0],
                }
            )
        else:
            action.update(
                {
                    "name": _("Analysis from %s", self.name),
                    "domain": [("id", "in", analysis_line_ids)],
                    "view_mode": "tree,form",
                }
            )
        return action

    def create_all_analysis(self):
        for line in self.move_line_nosuggest_ids:
            if line.is_product_sample and line.product_id.quality_check_ids:
                for quality_check in line.product_id.quality_check_ids:
                    if quality_check.analysis_ids:
                        for analysis in quality_check.analysis_ids:
                            if not self.env["analysis.line.lims"].search(
                                [
                                    ("stock_move_line_id", "=", line.id),
                                    ("analysis_id", "=", analysis.id),
                                    ("lot_id", "=", line.lot_id.id),
                                ]
                            ):
                                valList = {
                                    "laboratory_id": 1,
                                    "stock_move_line_id": line.id,
                                    "analysis_id": analysis.id,
                                    "customer_id": self.partner_id.id,
                                    "customer_contact_id": self.partner_id.id,
                                    "lot_id": line.lot_id.id,
                                }
                                self.env["analysis.line.lims"].create(valList)
