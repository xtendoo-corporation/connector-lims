# Copyright 2021 - Manuel Calero https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
import datetime

from odoo import models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    def _action_confirm(self):
        result = super(SaleOrder, self)._action_confirm()
        for order in self:
            order.order_line.sudo()._purchase_sample_generation()
        return result


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    def _purchase_sample_create(self):
        sale_line_purchase_map = {}
        for line in self:
            line = line.with_company(line.company_id)
            # determine vendor of the order (take the first matching company and product)
            purchase_order = self._get_purchase_order(line)
            # add a PO line to the PO
            values = line._purchase_sample_prepare_line_values(purchase_order)
            line.env["purchase.order.line"].create(values)
            return sale_line_purchase_map

    def _get_purchase_order(self, line):
        PurchaseOrder = self.env["purchase.order"]
        purchase_order = PurchaseOrder.search(
            [
                ("partner_id", "=", line.order_id.partner_id.id),
                ("state", "=", "draft"),
                ("company_id", "=", line.company_id.id),
            ],
            limit=1,
        )
        if purchase_order:
            return purchase_order
        return self._create_purchase_order(line)

    def _create_purchase_order(self, line):
        PurchaseOrder = self.env["purchase.order"]
        values = line._purchase_sample_prepare_order_values(line.order_id.partner_id)
        purchase_order = PurchaseOrder.create(values)
        return purchase_order

    def _purchase_sample_generation(self):
        """Create a Purchase for the first time
        from the sale line.
         If the SO line already created a PO, it
        will not create a second one.
        """
        sale_line_purchase_map = {}
        for line in self:
            # Do not regenerate PO line if the SO line has already
            # created one in the past (SO cancel/reconfirmation case)
            if line.product_id.is_product_sample:
                if not line.purchase_line_count:
                    result = line._purchase_sample_create()
                    sale_line_purchase_map.update(result)
        return sale_line_purchase_map

    def _purchase_sample_prepare_order_values(self, supplierinfo):
        self.ensure_one()
        date_order = datetime.datetime.now()
        return {
            "partner_id": supplierinfo.id,
            "partner_ref": supplierinfo.ref,
            "company_id": self.company_id.id,
            "currency_id": supplierinfo.property_purchase_currency_id.id
            or self.env.company.currency_id.id,
            "dest_address_id": False,  # False since only supported in stock
            "origin": self.order_id.name,
            "payment_term_id": supplierinfo.property_supplier_payment_term_id.id,
            "date_order": date_order,
        }

    def _purchase_sample_prepare_line_values(self, purchase_order, quantity=False):
        self.ensure_one()
        # compute quantity from SO line UoM
        product_quantity = self.product_uom_qty
        purchase_qty_uom = self.product_uom._compute_quantity(
            product_quantity, self.product_id.uom_po_id
        )
        price_unit = 0.0
        date_planned = datetime.datetime.now()
        return {
            "name": "[%s] %s" % (self.product_id.default_code, self.name)
            if self.product_id.default_code
            else self.name,
            "product_qty": purchase_qty_uom,
            "product_id": self.product_id.id,
            "product_uom": self.product_id.uom_po_id.id,
            "price_unit": price_unit,
            "date_planned": date_planned,
            "taxes_id": None,
            "order_id": purchase_order.id,
            "sale_line_id": self.id,
        }
