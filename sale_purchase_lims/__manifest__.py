# Copyright 2021 - Manuel Calero <https://xtendoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "Sale Purchase LIMS",
    "summary": "Sale based on LIMS products.",
    "version": "14.0.1.0.1",
    "license": "AGPL-3",
    "author": "Xtendoo, Odoo Community Association (OCA)",
    "category": "Warehouse",
    "website": "https://github.com/OCA/connector-lims",
    "depends": [
        "sale",
        "purchase",
        "sale_purchase",
        "product_attribute_lims",
    ],
    "data": [
        "data/mail_data.xml",
        "views/product_views.xml",
        "views/sale_order_views.xml",
        "views/purchase_order_views.xml",
    ],
    "installable": True,
}
