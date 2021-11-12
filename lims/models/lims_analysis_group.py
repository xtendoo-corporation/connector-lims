# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LimsAnalysisGroup(models.Model):
    _name = "lims.analysis.group"
    _description = "Quality Check"
    name = fields.Char(string="Name", store=True)
    # analysis_ids = fields.One2many(
    #     "lims.analysis",
    #     "analysis_group_ids",
    # )
    analysis_ids = fields.Many2many(
        "lims.analysis",
        "lims_analysis_group_lims_analysis_rel",
        "analysis_group_id",
        "analysis_id",
        string="Analysis",
    )
    # product_ids = fields.Many2one(
    #     "product.template",
    #     "Products",
    #     invisible=True,
    # )
    product_ids = fields.Many2many(
        "product.template",
        "product_template_lims_analysis_group_rel",
        "product_id",
        "analysis_group_id",
        "Products",
    )
