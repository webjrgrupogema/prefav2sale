# -*- coding: utf-8 -*-
from odoo import api, fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def prefacturate_order(self):
        # Lógica para prefacturar la orden de venta
        # Puedes agregar aquí la lógica para crear la prefactura y realizar cualquier otra acción necesaria

        # Ejemplo: Cambiar el estado de la orden de venta a "Prefacturada"
        self.write({'state': 'prefacturated'})

        return {
            'name': 'Prefacturación',
            'type': 'ir.actions.act_window',
            'res_model': 'sale.order',  # Reemplaza por el modelo de prefactura si es diferente
            'view_mode': 'form',
            'res_id': self.id,
        }