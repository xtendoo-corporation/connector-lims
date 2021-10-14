# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    have_quality_check = fields.Boolean(
        string="Have quality check",
        compute="_compute_have_quality_checks",
    )

    def _compute_have_quality_checks(self):
        self.have_quality_check = False
        for line in self.move_ids_without_package:
            if not line.product_id.quality_checks_ids:
                self.have_quality_check = True
