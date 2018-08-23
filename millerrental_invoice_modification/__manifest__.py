# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Millerrental Account Customization",
    'summary': "Adding Some fields on Invoice line",
    'description': """
- Adding Bin#, PO#, Date, and Location fields on Invoice line
- Invoice report customization
        """,
    'author': "odoo, inc",
    'website': "http://www.odoo.com",
    'category': 'Account',
    'version': '0.1',
    'depends': ['account_accountant', 'purchase', 'sale'],
    'data': [
        'views/account_views.xml',
        'views/report_invoice_inherit.xml',
    ],
}
