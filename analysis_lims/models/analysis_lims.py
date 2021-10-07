# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AnalysisLims(models.Model):
    _name = "analysis.lims"
    _description = "Analysis LIMS"

    # Sample information
    name = fields.Char(compute="_compute_analysis_name", string="Name", store=True)

    description = fields.Char(string="Description", store=True)

    product_id = fields.Many2one(
        comodel_name="product.template",
        string="Product",
        required=True,
        readonly=True,
    )

    lot_id = fields.Many2one(
        comodel_name="stock.production.lot",
        string="Lot",
        required=True,
        readonly=True,
    )

    # Partnter Analysis
    priority = fields.int(
        string="Priority", store=True
    )  # Ver como restringir a 1, 2 y 3

    is_duplicate = fields.bool(string="Is Duplicate", store=True)

    all_test_received = fields.bool(string="All Test Received", store=True)

    change = fields.bool(string="Change", store=True)

    # Request
    is_locked = fields.bool(string="Is Locked", store=True)

    incomplete = fields.bool(string="Incomplete", store=True)

    out_of_time = fields.bool(string="Out Of Time", store=True)
