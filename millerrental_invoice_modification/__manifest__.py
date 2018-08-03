# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Millerrental Account Customization",
    'summary': "Adding Some fields on line",
    'description': "Adding Bin#, PO#, Date, and Location fields on Invoice line",
    'author': "odoo, inc",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['account_accountant', 'purchase'],

    # always loaded
    'data': [
        'views/account_views.xml',
        'views/report_invoice_inherit.xml',
    ],
}

