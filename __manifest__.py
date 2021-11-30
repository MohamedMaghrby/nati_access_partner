# -*- coding: utf-8 -*-
{
    'name': "Nati Access Partner",
    'summary': """
      access rules for contacts """,

    'description': """
      how to show and access to contact for  users
      """,
    'author': "Mali, MuhlhelITS",
    'website': "http://muhlhel.com",
    'price': 1000.00,
    'currency': 'USD',
    'license': 'OPL-1',
    'category': 'Tools',
    'version': '15.0.0.0',

    # any module necessary for this one to work correctly
    'depends': [
        'base',
    ],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/res_partner.xml',
        'views/res_partner.xml',
        'wizards/res_partner_access.xml',
        'wizards/res_partner_unaccess.xml',

    ],
    'images': ['static/description/banner.png'],
    'installable': True,
}
