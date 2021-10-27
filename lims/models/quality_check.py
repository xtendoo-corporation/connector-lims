# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class QualityCheck(models.Model):
    _name = "quality.check"
    _description = "Quality Check"
    name = fields.Char(string="Name", store=True)
    analysis_ids = fields.One2many(
        "analysis.lims",
        "quality_check_ids",
    )
    product_ids = fields.Many2one(
        "product.template",
        "Products",
        invisible=True,
    )
