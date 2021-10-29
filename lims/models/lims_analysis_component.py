# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LimsAnalysisComponent(models.Model):
    _name = "lims.analysis.component"
    _description = "Component LIMS"
    analysis_ids = fields.Many2one(
        "lims.analysis",
        "Analysis lims",
    )
    name = fields.Char(string="Name", store=True)

    component_limit_result_ids = fields.One2many(
        "lims.analysis.component.limit.result",
        "component_ids",
    )
