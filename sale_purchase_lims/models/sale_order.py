# Copyright 2021 - Manuel Calero <https://xtendoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _action_confirm(self):
        result = super(SaleOrder, self)._action_confirm()
        for order in self:
            order.order_line.sudo()._purchase_service_generation()
        return result


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _purchase_service_generation(self):
        """Create a Purchase for the first time
        from the sale line.
         If the SO line already created a PO, it
        will not create a second one.
        """
        sale_line_purchase_map = {}
        for line in self:
            # Do not regenerate PO line if the SO line has already
            # created one in the past (SO cancel/reconfirmation case)
            if not line.product_id.is_product_sample:
                result = line._purchase_service_create()
                if line.product_id.service_to_purchase and not line.purchase_line_count:
                    sale_line_purchase_map.update(result)
            else:
                result = line._purchase_service_create_sample()
                if line.product_id.service_to_purchase and not line.purchase_line_count:
                    sale_line_purchase_map.update(result)
            return sale_line_purchase_map

    def _purchase_service_create_sample(self):
        sale_line_purchase_map = {}
        return sale_line_purchase_map
