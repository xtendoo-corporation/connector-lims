# Copyright 2021 - Daniel Domínguez https://xtendoo.es/
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AnalysisLineLims(models.Model):
    _name = "analysis.line.lims"
    _description = "Analysis Line LIMS"

    name = fields.Char(string="Name", store=True)

    analysis_id = fields.Many2one(
        "analysis.lims",
        "Analysis",
        invisible=True,
    )

    stock_move_line_id = fields.Many2one(
        "stock.move.line",
        "Stock Move line",
    )

    # Partner Analysis campo por si pertenece a un analisis padre
    # analysis_ids = fields.One2many("analysis.lims", "analysis_line_ids", invisible=True)
    #
    # priority = fields.Selection(
    #     [("1", "Low"), ("2", "Medium"), ("3", "High")], "Priority", size=1, default="1"
    # )
    # is_duplicate = fields.Boolean(string="Is Duplicate", store=True)
    #
    # all_test_received = fields.Boolean(string="All Test Received", store=True)
    #
    # change = fields.Boolean(string="Change", store=True)

    # Request
    # is_locked = fields.Boolean(string="Is Locked", store=True)
    #
    # incomplete = fields.Boolean(string="Incomplete", store=True)
    #
    # out_of_time = fields.Boolean(string="Out Of Time", store=True)

    # Sample information
    # sample_name = fields.Char(string="Name", store=True)
    #
    # description = fields.Char(string="Description", store=True)
    #
    # product_id = fields.Many2one(
    #     comodel_name="product.template",
    #     string="Sample",
    # )
    #
    # lot_id = fields.Many2one(
    #     comodel_name="stock.production.lot",
    #     string="Lot",
    # )
    # Campo matrix indicara el conjunto de test al que pertenede
    # Matrix

    # Campo para registrar la regulacion
    # Regulation

    # General Information

    # laboratory_id = fields.Many2one(
    #     comodel_name="res.partner",
    #     string="Laboratory",
    #     required=True,
    # )
    #
    # customer_id = fields.Many2one(
    #     comodel_name="res.partner",
    #     string="Customer",
    # )
    #
    # customer_contact_id = fields.Many2one(
    #     comodel_name="res.partner",
    #     string="Customer contact",
    # )
    #
    # reason = fields.Char(string="Reason", store=True)
    #
    # reference = fields.Char(string="Reference", store=True)
    #
    # is_locked = fields.Boolean(string="Active", store=True)

    # Ver que tags llevaran a que tabla conectarlo
    # tag_ids = fields.Many2one(
    #     comodel_name="",
    #     string="Tag",
    # )

    # Sampling information

    # date_plan = fields.Date(string="Date planned")
    # date_due = fields.Date(string="Date due")
    #
    # date_sample = fields.Date(string="Date sample")
    #
    # date_sample_receipt = fields.Date(string="Date sample receipt")
    #
    # date_sample_begin = fields.Date(string="Date sample begin")
    # # Poner deffault el user_id activo
    # sampler = fields.Many2one(
    #     comodel_name="res.user",
    #     string="Sampler",
    # )
