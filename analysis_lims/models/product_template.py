# Copyright 2021 - Manuel Calero <https://xtendoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    have_analysis = fields.Boolean(
        string="Have analysis",
        default=False,
    )
    quality_checks_ids = fields.Many2many(
        "quality.checks.lims",
        "product_quality_cheks_lims_rel",
        "product_id",
        "quality_check_id",
        string="Quality Checks",
    )

    quality_checks_ids = fields.One2many(
        "quality.checks.lims", "product_ids", string="Quality Checks"
    )
