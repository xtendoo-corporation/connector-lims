# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class LimsAnalysisLine(models.Model):
    _name = "lims.analysis.line"
    _inherit = ["mail.thread"]
    _description = "Analysis Line LIMS"
    name = fields.Char(string="Name", store=True, readonly="1")
    analysis_id = fields.Many2one(
        "lims.analysis",
        "Analysis",
        invisible=True,
        tracking=True,
    )
    numerical_result = fields.One2many(
        "lims.analysis.numerical.result",
        "analysis_ids",
        tracking=True,
    )
    stock_move_line_id = fields.Many2one(
        "stock.move.line",
        "Stock Line Move",
        default=lambda self: self.env.context.get("stock_move_line_id"),
        tracking=True,
    )
    product_id = fields.Many2one(
        "product.template",
        "Products",
        default=lambda self: self.env.context.get("product_id"),
        tracking=True,
    )
    priority = fields.Selection(
        [("0", "Normal"), ("1", "Low"), ("2", "Medium"), ("3", "High")],
        "Priority",
        default="1",
        tracking=True,
    )
    state = fields.Selection(
        [
            ("cancel", "Cancel"),
            ("received", "Received"),
            ("started", "Started"),
            ("complete", "Complete"),
            ("validated", "Validated"),
            ("issued", "Issued"),
        ],
        "State",
        default="received",
        tracking=True,
    )
    result = fields.Selection(
        [
            ("none", "Unrealized"),
            ("pass", "Approved"),
            ("fail", "Failed"),
            ("warning", "Warning"),
        ],
        "Result",
        default="none",
        tracking=True,
    )
    is_duplicate = fields.Boolean(string="Is Duplicate", store=True)
    all_test_received = fields.Boolean(string="All Test Received", store=True)
    change = fields.Boolean(string="Change", store=True)
    # Request
    is_locked = fields.Boolean(string="Is Locked", store=True)
    incomplete = fields.Boolean(string="Incomplete", store=True)
    out_of_time = fields.Boolean(string="Out Of Time", store=True)
    # Sample information
    sample_name = fields.Char(
        string="Sample Name",
        store=True,
        tracking=True,
    )
    description = fields.Char(
        string="Description",
        store=True,
        tracking=True,
    )
    lot_id = fields.Many2one(
        comodel_name="stock.production.lot",
        string="Lot",
        default=lambda self: self.env.context.get("lot_id"),
        tracking=True,
    )
    # Campo matrix indicara el conjunto de test al que pertenede
    # Matrix

    # Campo para registrar la regulacion
    # Regulation

    # General Information
    laboratory_id = fields.Many2one(
        comodel_name="res.partner",
        string="Laboratory",
        tracking=True,
    )
    customer_id = fields.Many2one(
        comodel_name="res.partner",
        string="Customer",
        default=lambda self: self.env.context.get("customer_id"),
        tracking=True,
    )
    customer_contact_id = fields.Many2one(
        comodel_name="res.partner",
        string="Customer contact",
        default=lambda self: self.env.context.get("customer_id"),
        tracking=True,
    )
    reason = fields.Char(
        string="Reason",
        store=True,
        tracking=True,
    )
    reference = fields.Char(
        string="Reference",
        store=True,
        tracking=True,
    )
    active = fields.Boolean(
        string="Active",
        store=True,
        default=True,
        tracking=True,
    )
    is_locked = fields.Boolean(
        string="Is Locked",
        store=True,
        tracking=True,
    )
    # Ver que tags llevaran a que tabla conectarlo
    # tag_ids = fields.Many2one(
    #    comodel_name="",
    #    string="Tag",
    # )
    # Sampling information
    date_plan = fields.Date(
        string="Date planned",
        tracking=True,
    )
    date_due = fields.Date(
        string="Date due",
        tracking=True,
    )
    date_sample = fields.Date(
        string="Date sample",
        tracking=True,
    )
    date_sample_receipt = fields.Date(
        string="Date sample receipt",
        tracking=True,
    )
    date_sample_begin = fields.Date(
        string="Date sample begin",
        tracking=True,
    )
    sampler = fields.Many2one(
        comodel_name="res.users",
        string="Sampler",
        default=lambda self: self.env.user.id,
        tracking=True,
    )

    @api.model
    def create(self, vals):
        if vals.get("name", "New") == "New":
            vals["name"] = (
                self.env["ir.sequence"].next_by_code("analysis.line.lims.code") or "/"
            )
            analysis_base_id = self.env["lims.analysis"].search(
                [
                    ("id", "=", vals.get("analysis_id")),
                ]
            )
            result = super(LimsAnalysisLine, self).create(vals)
            for parameter in analysis_base_id.parameter_ids:
                self.env["lims.analysis.numerical.result"].create(
                    {
                        "analysis_ids": result.id,
                        "parameter_ids": parameter.id,
                        "limit_value": parameter._get_limit_value(),
                        "limit_value_char": parameter._get_limit_value_char(),
                        "between_limit_value": parameter._get_between_limit_value(),
                    }
                )

        return result

    def toggle_active(self):
        res = super().toggle_active()
        if self.filtered(lambda so: so.state not in ["draft", "cancel"]):
            raise UserError(_("Only 'Draft' or 'Canceled' orders can be archived"))
        return res

    def action_confirm(self):
        if self.filtered(lambda self: self.state != "draft"):
            raise UserError(_("You can only confirm draft analysis"))
        res = self.write({"state": "to-do"})
        return res

    def action_cancel(self):
        if self.filtered(lambda self: self.state not in ["to-do", "draft"]):
            raise UserError(_("You can only cancel Confirm analysis"))
        res = self.write({"state": "cancel"})
        return res

    def action_draft(self):
        if self.filtered(lambda self: self.state not in ["to-do", "cancel"]):
            raise UserError(_("You can only draft Confirm analysis"))
        res = self.write({"state": "draft"})
        return res

    def action_analysis(self):
        if self.filtered(lambda self: self.result != "none"):
            raise UserError(_("You can only to realize analysis Unrealized Analysis"))
        # TO-DO: Realizar el analisis y cambiar el result.
        analysis_result = "fail"
        result_value = []
        for result in self.numerical_result:
            analysis_result = result._get_value_result(result.value)
            result_value.append(analysis_result)
        for line in result_value:
            if line == "fail":
                analysis_result = line
                break
            if line == "warning":
                analysis_result = line
        res = self.write({"state": "done", "result": analysis_result})
        return res
