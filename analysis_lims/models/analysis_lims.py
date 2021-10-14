# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AnalysisLims(models.Model):
    _name = "analysis.lims"
    _description = "Analysis LIMS"
    # Partner Analysis campo por si pertenece a un analisis padre
    quality_check_ids = fields.Many2one(
        "quality.checks.lims", "Quality Checks", invisible=True
    )

    name = fields.Char(string="Name", store=True)

    analysis_line_ids = fields.One2many(
        "analysis.line.lims", "analysis_ids", invisible=True
    )
