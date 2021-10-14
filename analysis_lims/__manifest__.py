# Copyright 2021 - Daniel Domínguez <https://xtendoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).
# Probando git
{
    "name": "Analysis LIMS",
    "summary": "Analysis LIMS.",
    "version": "14.0.1.0.1",
    "license": "AGPL-3",
    "author": "Xtendoo, Odoo Community Association (OCA)",
    "category": "Warehouse",
    "website": "https://github.com/OCA/connector-lims",
    "depends": [
        "sale_purchase_lims",
        "product_attribute_lims",
    ],
    "data": [
        "views/quality_checks_lims_views.xml",
        "views/analysis_lims_views.xml",
        "views/analysis_line_lims_views.xml",
        "views/stock_picking_view.xml",
        "views/product_view.xml",
        "security/ir.model.access.csv",
    ],
    "installable": True,
}
