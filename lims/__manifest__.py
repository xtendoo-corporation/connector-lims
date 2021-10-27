# Copyright 2017-2019 MuK IT GmbH
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Laboratory Information Management System",
    "summary": """Laboratory Information Management System for Odoo""",
    "version": "14.0.4.0.1",
    "category": "Laboratory Information Management",
    "license": "LGPL-3",
    "website": "https://github.com/OCA/connector-lims",
    "author": "Xtendoo, Odoo Community Association (OCA)",
    "depends": [
        "base",
        "sale",
        "purchase",
        "stock",
        "product",
    ],
    "data": [
        "security/ir.model.access.csv",
        "views/product_template_view.xml",
        "views/stock_move_line_views.xml",
        "views/analysis_components_views.xml",
        "views/menu.xml",
        "views/analysis_lims_views.xml",
        "views/analysis_line_lims_views.xml",
        "views/res_config_settings.xml",
        "views/quality_check_views.xml",
        "views/stock_picking_view.xml",
        "views/res_partner.xml",
    ],
    "images": ["static/description/banner.png"],
    "application": True,
}
