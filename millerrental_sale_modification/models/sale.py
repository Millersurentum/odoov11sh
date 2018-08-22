# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from datetime import datetime, timedelta


class SaleOrder(models.Model):
    _inherit = "sale.order"

    start_date = fields.Date(string="Start Date", default=fields.Date.context_today, store=True)
    end_date = fields.Date(string="End Date", store=True)

    @api.onchange('start_date', 'end_date')
    def _onchange_date(self):
        self.ensure_one()
        for line in self.order_line.filtered(lambda l: l.product_id.recurring_invoice):
            line.start_date = line.order_id.start_date
            line.end_date = line.order_id.end_date
            line._get_product_qty(line.start_date, line.end_date)

    @api.multi
    def action_confirm(self):
        self.ensure_one()
        res = super(SaleOrder, self).action_confirm()
        for line in self.order_line:
            move = line.env['stock.move'].search([('sale_line_id', '=', line.id), ('created_purchase_line_id', '!=', False)], limit=1)
            line.po = move.created_purchase_line_id.order_id.name
        return res


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    po = fields.Char(string="PO #")
    start_date = fields.Date(string="Start Date", default=fields.Date.context_today, store=True)
    end_date = fields.Date(string="End Date", store=True)

    def _get_product_qty(self, start_date, end_date):
        from_date = fields.Datetime.from_string(self.start_date)
        to_date = fields.Datetime.from_string(self.end_date)
        if to_date and from_date:
            delta = to_date - from_date
            self.product_uom_qty = delta.days

    @api.onchange('product_id', 'start_date', 'end_date')
    def _compute_qty(self):
        for line in self.filtered(lambda l: l.product_id.recurring_invoice):
            line.start_date = line.order_id.start_date
            line.end_date = line.order_id.end_date
            line._get_product_qty(line.start_date, line.end_date)
