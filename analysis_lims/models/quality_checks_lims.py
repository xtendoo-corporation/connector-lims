# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class QualityChecksLims(models.Model):
    _name = "quality.checks.lims"
    _description = "Quality Checks LIMS"

    name = fields.Char(
        string="Name",
        store=True,
        required=True,
    )
    # product_ids = fields.One2many(
    #     "product.template",
    #     "quality_checks_ids",
    #     invisible=True,
    # )
    # analysis_id = fields.Many2one(
    #     "analysis.lims",
    #     string="Quality Checks",
    # )
    # lot_id = fields.Many2one(
    #     comodel_name="stock.production.lot",
    #     string="Lot",
    # )
    # checked_date = fields.Date(string="Checked planned")
    #
    # checked_by = fields.Many2one(
    #     comodel_name="res.user",
    #     string="Cecked By",
    # )
    #
    # status = fields.Selection(
    #     [("1", "To do"), ("2", "In Progress"), ("3", "Done")],
    #     "Status",
    #     size=1,
    #     default="1",
    # )
