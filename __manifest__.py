# -*- coding: utf-8 -*-
{
    'name': "prefav2sale",

    'summary': 'Modulo personalizado  y de vista extendida para el modulo de ventas',

    'description': 'Modulo personalizado  y de vista extendida para el modulo de ventas, donde pasara de una vista a otra vista.',

    'author': "All Service Rhyno S.A.S",
    'website': "https://allser.com.co",


    'category': 'Sales',
    'version': '1.0',

    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'views/sale_order_view.xml',
        'views/menuprefactura.xml',
    ],

    'installable': True,
}
