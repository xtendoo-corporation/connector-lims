# Copyright 2022 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LimsAnalyticalMethod(models.Model):
    _name = "lims.analytical.method"
    _description = "Analytical Method"

    default_code = fields.Char("Reference", index=True)
    name = fields.Char(string="Name", store=True)
    description = fields.Char(string="Description", store=True)
    method_uom = fields.Many2one(
        "uom.uom",
        string="Unit of Measure",
    )

    uncertainty = fields.Float(string="uncertainty", store=True)

    _sql_constraints = [
        ("code_uniq", "unique (default_code)", "Code already exists!"),
    ]
