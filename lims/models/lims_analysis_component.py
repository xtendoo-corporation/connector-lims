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

    def _get_limit_value(self):
        limit_result = 0.00
        for component_line in self.component_limit_result_ids:
            if component_line.type == "LIMIT" and component_line.state == "conform":
                limit_result = component_line.limit_value_to
        return limit_result

    def _get_between_limit_value(self):
        between_limit_result = ""
        for component_line in self.component_limit_result_ids:
            if component_line.type == "BETWEEN" and component_line.state == "conform":
                between_limit_result = ("{value_from: .2f} and {value_to: .2f}").format(
                    value_from=component_line.limit_value_from,
                    value_to=component_line.limit_value_to,
                )
        return between_limit_result
