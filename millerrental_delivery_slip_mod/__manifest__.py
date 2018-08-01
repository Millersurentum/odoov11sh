# -*- coding: utf-8 -*-
{
    'name': "Millerrental Delivery Reports",

    'summary': "Adding agreement/signature to delivery slip",

    'description': "Adding an agreement and signature section to the Delivery Slip Report",

    'author': "odoo, inc",
    'website': "http://www.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['stock', 'web'],

    # always loaded
    'data': [
        'report/custom_assets.xml',
        'report/delivery_slip_mod.xml',
    ],
    'auto_install': True,
}
