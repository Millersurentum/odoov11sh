# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from datetime import datetime, timedelta


class SaleOrder(models.Model):
    _inherit = "sale.order"

    start_date = fields.Date(string="Start Date", default=fields.Date.context_today, store=True)
    end_date = fields.Date(string="End Date", default=datetime.today() + timedelta(days=5), store=True)

    @api.onchange('start_date', 'end_date')
    def _onchange_date(self):
        self.ensure_one()
        for line in self.order_line:
            line.start_date = line.order_id.start_date
            line.end_date = line.order_id.end_date
            line._get_product_qty(line.start_date, line.end_date)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    po = fields.Char(string="PO #")
    start_date = fields.Date(string="Start Date", default=fields.Date.context_today, store=True)
    end_date = fields.Date(string="End Date", default=datetime.today() + timedelta(days=5), store=True)

    def _get_product_qty(self, start_date, end_date):
        from_date = datetime.strptime(self.start_date, '%Y-%m-%d').date()
        to_date = datetime.strptime(self.end_date, '%Y-%m-%d').date()
        delta = to_date - from_date
        self.product_uom_qty = delta.days

    @api.onchange('product_id', 'start_date', 'end_date', 'order_id.start_date')
    def _compute_qty(self):
        for line in self:
            line._get_product_qty(line.start_date, line.end_date)
