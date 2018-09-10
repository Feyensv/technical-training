# -*- coding: utf-8 -*-
{
    'name':        "Library Management",

    'summary':
                   """
                   Library management
                   """,

    'description': """
        Manage a Library: customers, books, etc....
    """,

    'author':      "Odoo",
    'website':     "http://www.odoo.com",

    'category':    'Library',
    'version':     '0.3',

    # any module necessary for this one to work correctly
    'depends':     ['base'],

    # always loaded
    'data':        [
        "security/ir.model.access.csv",
    ],
    # only loaded in demonstration mode
    'demo':        [
        "data/library_demo.xml",
    ],
}
