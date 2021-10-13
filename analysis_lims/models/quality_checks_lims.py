# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class QualityChecksLims(models.Model):
    _name = "quality.checks.lims"
    _description = "Quality Checks LIMS"

    name = fields.Char(string="Name", store=True, required=True)

    product_ids = fields.Many2one("product.template", "Product")

    # Crear relacion con los analisis
