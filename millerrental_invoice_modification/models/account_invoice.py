# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields


class AccountInvoiceLine(models.Model):
    _inherit = "account.invoice.line"

    bin_line = fields.Char(string="Bin #")
    line_po = fields.Char(string="PO #")
    start_date = fields.Date(string="Start Date")
    end_date = fields.Date(string="End Date")
