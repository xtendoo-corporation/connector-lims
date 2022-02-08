# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ProductionLot(models.Model):
    _inherit = "stock.production.lot"

    product_id = fields.Many2one(
        "product.product",
        "Product",
        domain=lambda self: self._domain_product_id(),
        required=False,
        check_company=True,
    )
