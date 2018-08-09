# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': "Millerrental Sale Customization",
    'summary': "SO screen customization",
    'description': """
1. Default Start date, Default End Date
2. PO#, Start Date, End Date at the SO line item level.  PO# to be captured in the SO printout as well.
3. On entering Start Date and End Date on the SO, the "Quantity" (duration) of the Container Rent
product on the Sale Order lines needs to be populated based on the date values entered.
        """,
    'author': "odoo, inc",
    'website': "http://www.odoo.com",
    'category': 'Account',
    'version': '0.1',
    'depends': ['sale_management'],
    'data': [
        'views/sale_report_inherit.xml',
        'views/sale_views.xml',
    ],
}
