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
        "views/res_partner.xml",
        "views/menu.xml",
        "views/lims_analysis_parameter_views.xml",
        "views/lims_analysis_parameter_limit_result_views.xml",
        "views/lims_analysis_numerical_result_views.xml",
        "views/lims_analysis_views.xml",
        "views/lims_analysis_line_views.xml",
        "views/res_config_settings.xml",
        "views/lims_analysis_group_views.xml",
        "views/stock_picking_view.xml",
        "wizards/wizard_lot.xml",
        "views/stock_production_lot_view.xml",
        "views/lims_analytical_method_views.xml",
        "views/sale_order_view.xml",
        # Formatos
        "views/label/label_print.xml",
        # js
        "templates/assets.xml",
    ],
    "images": ["static/description/banner.png"],
    "application": True,
}
