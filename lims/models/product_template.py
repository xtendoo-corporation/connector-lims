# Copyright 2021 - Manuel Calero <https://xtendoo.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    is_product_sample = fields.Boolean(
        string="Is a product sample",
        default=False,
    )
    analysis_group_ids = fields.One2many(
        "lims.analysis.group",
        "product_ids",
        invisible=True,
    )
    analysis_count = fields.Integer(
        "Number of Analysis Generated",
        compute="_compute_analysis_count",
    )

    @api.constrains("is_product_sample", "type")
    def _check_is_product_sample(self):
        if self.is_product_sample and self.type != "product":
            raise ValidationError(
                _("You can only create sample products if they are storable.")
            )
        self.tracking = "lot"

    def _compute_analysis_count(self):
        for order in self:
            order.analysis_count = len(self._get_analysis())

    def _get_analysis(self):
        return self.env["lims.analysis.line"].search([("product_id", "=", (self.id))])

    def action_view_analysis(self):
        self.ensure_one()
        analysis_line_ids = self._get_analysis().ids
        action = {
            "res_model": "lims.analysis.line",
            "type": "ir.actions.act_window",
        }
        if len(analysis_line_ids) == 1:
            action.update(
                {
                    "view_mode": "form",
                    "res_id": analysis_line_ids[0],
                }
            )
        else:
            action.update(
                {
                    "name": _("Analysis from Product %s", self.name),
                    "domain": [("id", "in", analysis_line_ids)],
                    "view_mode": "tree,form",
                }
            )
        return action
