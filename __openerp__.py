# -*- coding: utf-8 -*-
# This file is part of Seedoo.  The COPYRIGHT file at the top level of
# this module contains the full copyright notices and license terms.
# © 2016 Jason Wu (jaronemo@msn.com). Add and Fix It
{
    'name': 'PDF Viewer Widget',
    'description': '''
This module add a pdf preview to binary data

This module works with odoo 8.0
''',
    'version': '8.0.1',
    'author': 'Innoviu Srl, Jason Wu(Jaronemo@msn.com)',
    'category': 'Usability',
    'website': 'https://www.innoviu.com, http://www.osstw.com',
    'license': 'AGPL-3',
    'depends': [
        'web',
        ],
    'python': ['magic'],
    'data': ['base_data.xml'],
    'js': ['static/src/js/web_pdf_widget.js'],
    'qweb': ['static/src/xml/web_pdf_widget.xml'],
    'installable': True,
    'auto_install': False,
}
