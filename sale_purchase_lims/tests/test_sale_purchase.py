# Copyright 2021 - Manuel Calero <https://xtendoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests.common import TransactionCase


class TestSalePurchase(TransactionCase):
    def setUp(self):
        super(TestSalePurchase, self).setUp()
        self.product_sample = self.env["product.product"].create(
            {
                "name": "Sample Product",
                "is_product_sample": True,
                "type": "product",
                "categ_id": self.env.ref("product.product_category_all").id,
            }
        )
        self.product_sample_2 = self.env["product.product"].create(
            {
                "name": "Sample Product 2",
                "is_product_sample": True,
                "type": "product",
                "categ_id": self.env.ref("product.product_category_all").id,
            }
        )
        self.partner = self.env["res.partner"].create(
            {
                "name": "Test",
            }
        )
        self.supplier = self.env["res.partner"].create(
            {
                "name": "Supplier Test",
            }
        )
        self.product_no_sample = self.env["product.product"].create(
            {
                "name": "Not Sample Product",
                "is_product_sample": False,
                "type": "product",
                "categ_id": self.env.ref("product.product_category_all").id,
            }
        )

        self.product_service_autopurchase = self.env["product.product"].create(
            {
                "name": "Service Product Autopurchase",
                "is_product_sample": False,
                "type": "service",
                "categ_id": self.env.ref("product.product_category_all").id,
                "service_to_purchase": True,
                "seller_ids": [
                    (
                        0,
                        0,
                        {
                            "name": self.supplier.id,
                            "price": 0.0,
                            "delay": 1,
                            "min_qty": 1,
                        },
                    )
                ],
            }
        )

    def test_create_sale_not_sample(self):
        order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "name": self.product_no_sample.name,
                            "product_id": self.product_no_sample.id,
                            "product_uom_qty": 1,
                            "product_uom": self.product_no_sample.uom_id.id,
                            "price_unit": 1000.00,
                        },
                    )
                ],
            }
        )
        order.action_confirm()
        purchase_order = self.env["purchase.order"].search(
            [("origin", "=", order.name)]
        )
        self.assertEqual(len(purchase_order), 0)

    def test_create_sale_sample(self):
        order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "name": self.product_sample.name,
                            "product_id": self.product_sample.id,
                            "product_uom_qty": 1,
                            "product_uom": self.product_sample.uom_id.id,
                            "price_unit": 1000.00,
                        },
                    )
                ],
            }
        )
        order.action_confirm()
        purchase_order = self.env["purchase.order"].search(
            [("origin", "=", order.name)]
        )
        self.assertEqual(len(purchase_order), 1)
        self.assertEqual(purchase_order.partner_id.id, order.partner_id.id)
        self.assertEqual(
            purchase_order.order_line[0].product_id.is_product_sample, True
        )

    def test_create_sale_service_to_purchase(self):
        order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
                "order_line": [
                    (
                        0,
                        0,
                        {
                            "name": self.product_service_autopurchase.name,
                            "product_id": self.product_service_autopurchase.id,
                            "product_uom_qty": 1,
                            "product_uom": self.product_service_autopurchase.uom_id.id,
                            "price_unit": 1000.00,
                        },
                    )
                ],
            }
        )
        order.action_confirm()
        purchase_order = self.env["purchase.order"].search(
            [("origin", "=", order.name)]
        )
        self.assertEqual(len(purchase_order), 1)
        self.assertEqual(purchase_order.partner_id.id, self.supplier.id)
        self.assertEqual(
            purchase_order.order_line[0].product_id.is_product_sample, False
        )

    def test_create_sale_2_samples(self):
        order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
            }
        )
        self.env["sale.order.line"].create(
            {
                "name": self.product_sample.name,
                "product_id": self.product_sample.id,
                "product_uom_qty": 1,
                "product_uom": self.product_sample.uom_id.id,
                "price_unit": 1000.00,
                "order_id": order.id,
            }
        )
        self.env["sale.order.line"].create(
            {
                "name": self.product_sample_2.name,
                "product_id": self.product_sample_2.id,
                "product_uom_qty": 1,
                "product_uom": self.product_sample_2.uom_id.id,
                "price_unit": 1000.00,
                "order_id": order.id,
            }
        )
        order.action_confirm()
        purchase_order = self.env["purchase.order"].search(
            [("origin", "=", order.name)]
        )
        self.assertEqual(len(purchase_order), 1)
        self.assertEqual(len(purchase_order.order_line), 2)
        self.assertEqual(purchase_order.partner_id.id, order.partner_id.id)
        self.assertEqual(
            purchase_order.order_line[0].product_id.is_product_sample, True
        )
        self.assertEqual(
            purchase_order.order_line[1].product_id.is_product_sample, True
        )

    def test_create_sale_not_sample_and_sample(self):
        order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
            }
        )
        self.env["sale.order.line"].create(
            {
                "name": self.product_no_sample.name,
                "product_id": self.product_no_sample.id,
                "product_uom_qty": 1,
                "product_uom": self.product_no_sample.uom_id.id,
                "price_unit": 1000.00,
                "order_id": order.id,
            }
        )
        self.env["sale.order.line"].create(
            {
                "name": self.product_sample.name,
                "product_id": self.product_sample.id,
                "product_uom_qty": 1,
                "product_uom": self.product_sample.uom_id.id,
                "price_unit": 1000.00,
                "order_id": order.id,
            }
        )
        order.action_confirm()
        purchase_order = self.env["purchase.order"].search(
            [("origin", "=", order.name)]
        )
        self.assertEqual(len(purchase_order), 1)
        self.assertEqual(len(purchase_order.order_line), 1)
        self.assertEqual(purchase_order.partner_id.id, order.partner_id.id)
        self.assertEqual(
            purchase_order.order_line[0].product_id.is_product_sample, True
        )

    def test_create_sale_service_autopurchase_and_sample(self):
        order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
            }
        )
        self.env["sale.order.line"].create(
            {
                "name": self.product_service_autopurchase.name,
                "product_id": self.product_service_autopurchase.id,
                "product_uom_qty": 1,
                "product_uom": self.product_service_autopurchase.uom_id.id,
                "price_unit": 1000.00,
                "order_id": order.id,
            }
        )
        self.env["sale.order.line"].create(
            {
                "name": self.product_sample.name,
                "product_id": self.product_sample.id,
                "product_uom_qty": 1,
                "product_uom": self.product_sample.uom_id.id,
                "price_unit": 1000.00,
                "order_id": order.id,
            }
        )
        order.action_confirm()
        purchase_order = self.env["purchase.order"].search(
            [("origin", "=", order.name)]
        )
        self.assertEqual(len(purchase_order), 2)
        self.assertEqual(len(purchase_order[0].order_line), 1)
        self.assertEqual(len(purchase_order[1].order_line), 1)
        self.assertEqual(purchase_order[1].partner_id.id, self.supplier.id)
        self.assertEqual(purchase_order[0].partner_id.id, order.partner_id.id)
        self.assertEqual(
            purchase_order[1].order_line[0].product_id.is_product_sample, False
        )
        self.assertEqual(
            purchase_order[0].order_line[0].product_id.is_product_sample, True
        )

    def test_create_sale_service_autopurchase_and_sample_and_not_sample(self):
        order = self.env["sale.order"].create(
            {
                "partner_id": self.partner.id,
            }
        )
        self.env["sale.order.line"].create(
            {
                "name": self.product_service_autopurchase.name,
                "product_id": self.product_service_autopurchase.id,
                "product_uom_qty": 1,
                "product_uom": self.product_service_autopurchase.uom_id.id,
                "price_unit": 1000.00,
                "order_id": order.id,
            }
        )
        self.env["sale.order.line"].create(
            {
                "name": self.product_sample.name,
                "product_id": self.product_sample.id,
                "product_uom_qty": 1,
                "product_uom": self.product_sample.uom_id.id,
                "price_unit": 1000.00,
                "order_id": order.id,
            }
        )
        self.env["sale.order.line"].create(
            {
                "name": self.product_no_sample.name,
                "product_id": self.product_no_sample.id,
                "product_uom_qty": 1,
                "product_uom": self.product_no_sample.uom_id.id,
                "price_unit": 1000.00,
                "order_id": order.id,
            }
        )
        order.action_confirm()
        purchase_order = self.env["purchase.order"].search(
            [("origin", "=", order.name)]
        )
        self.assertEqual(len(purchase_order), 2)
        self.assertEqual(len(purchase_order[0].order_line), 1)
        self.assertEqual(len(purchase_order[1].order_line), 1)
        self.assertEqual(purchase_order[1].partner_id.id, self.supplier.id)
        self.assertEqual(purchase_order[0].partner_id.id, order.partner_id.id)
        self.assertEqual(
            purchase_order[1].order_line[0].product_id.is_product_sample, False
        )
        self.assertEqual(
            purchase_order[0].order_line[0].product_id.is_product_sample, True
        )
