# Copyright 2021 - Manuel Calero <https://xtendoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    quality_checks_ids = fields.Many2one(
        "quality.checks.lims",
        string="Quality Checks",
    )
