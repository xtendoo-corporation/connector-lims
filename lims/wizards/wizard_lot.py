from odoo import fields, models


class LotWiward(models.TransientModel):
    _name = "lims.wizard.lot"

    def _compute_number_from(self):
        return (
            self.env["ir.sequence"]
            .search([("code", "=", "stock.lot.serial")])
            .number_next_actual
        )

    number_from = fields.Integer(string="Primer Lote", default=_compute_number_from)
    quantity = fields.Integer(string="Cantidad", default="1")

    def generate_lots(self):
        lots = []
        for _ in range(self.quantity):
            lot_create = (
                self.env["stock.production.lot"]
                .sudo()
                .create(
                    {
                        "name": self.env["ir.sequence"].next_by_code("stock.lot.serial")
                        or "/",
                        "company_id": self.env.company.id,
                    }
                )
            )
            lots.append(lot_create.id)
        return lots

    def generate_and_print_lots(self):
        lots = self.generate_lots()
        lots_ids = self.env["stock.production.lot"].search([("id", "in", lots)])
        return self.env.ref("lims.lims_report_label_lot").report_action(lots_ids)
