# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class LimsAnalysis(models.Model):
    _name = "lims.analysis"
    _description = "Analysis LIMS"
    name = fields.Char(string="Name", store=True)
    description = fields.Char(string="Description", store=True)
    # analysis_group_ids = fields.Many2one(
    #     "lims.analysis.group",
    #     "Analysis Group",
    #     invisible=True,
    # )
    analysis_group_ids = fields.Many2many(
        "lims.analysis.group",
        "lims_analysis_group_lims_analysis_rel",
        "analysis_id",
        "analysis_group_id",
        "Analysis Group lims",
    )
    # parameter_ids = fields.One2many(
    #     "lims.analysis.parameter",
    #     "analysis_ids",
    # )

    parameter_ids = fields.Many2many(
        "lims.analysis.parameter",
        "lims_analysis_lims_analysis_parameter_rel",
        "analysis_id",
        "parameter_id",
        string="Parameters",
    )
