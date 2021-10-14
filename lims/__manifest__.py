# Copyright 2017-2019 MuK IT GmbH
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Laboratory Information Management System",
    "summary": """Laboratory Information Management System for Odoo""",
    "version": "14.0.4.0.1",
    "category": "Laboratory Information Management",
    "license": "LGPL-3",
    "website": "https://github.com/OCA/lims",
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
        "views/menu.xml",
        "views/res_config_settings.xml",
    ],
    "images": ["static/description/banner.png"],
    "application": True,
}
