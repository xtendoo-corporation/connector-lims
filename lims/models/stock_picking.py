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
        return self.env["lims.analysis.line"].search(
            [("stock_move_line_id", "in", (self.move_line_nosuggest_ids.ids))]
        )

    def action_view_analysis(self):
        self.ensure_one()
        analysis_line_ids = self._get_analysis().ids
        action = {
            "res_model": "lims.analysis.line",
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
            if line.is_product_sample and line.product_id.analysis_group_ids:
                for analysis_group in line.product_id.analysis_group_ids:
                    if analysis_group.analysis_ids:
                        for analysis in analysis_group.analysis_ids:
                            if not self.env["lims.analysis.line"].search(
                                [
                                    ("stock_move_line_id", "=", line.id),
                                    ("analysis_id", "=", analysis.id),
                                    ("lot_id", "=", line.lot_id.id),
                                ]
                            ):
                                analysis_id = self.env["lims.analysis.line"].create(
                                    {
                                        "product_id": line.product_id.product_tmpl_id.id,
                                        "stock_move_line_id": line.id,
                                        "analysis_id": analysis.id,
                                        "customer_id": self.partner_id.id,
                                        "customer_contact_id": self.partner_id.id,
                                        "lot_id": line.lot_id.id,
                                    }
                                )
                                for component in analysis.component_ids:
                                    self.env["lims.analysis.numerical.result"].create(
                                        {
                                            "analysis_ids": analysis_id.id,
                                            "component_ids": component.id,
                                            "limit_value": 5.0,
                                        }
                                    )
