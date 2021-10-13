# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

from odoo import models


class StockPicking(models.Model):
    _inherit = "stock.picking"

    def quality_checks(self):
        for line in self.move_ids_without_package:
            if line.product_id.have_analysis:
                # print(
                #    "*******************Funciona el button*****************",
                #    line.product_id.have_analysis,
                # )
                return
