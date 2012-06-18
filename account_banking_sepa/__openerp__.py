##############################################################################
#
#    SEPA PAIN module for OpenERP
#    Copyright (C) 2010-2012 Akretion (http://www.akretion.com)
#    @author: Alexis de Lattre <alexis.delattre@akretion.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Account Banking SEPA',
    'version': '0.1',
    'license': 'AGPL-3',
    'author': 'Akretion',
    'website': 'http://www.akretion.com',
    'category': 'Banking addons',
    'depends': ['account_banking'],
    'init_xml': [],
    'update_xml': [
        'account_banking_sepa_view.xml',
        'wizard/export_sepa_view.xml',
        'data/payment_type_sepa_sct.xml',
        'security/ir.model.access.csv',
    ],
    'demo_xml': [],
    'description': '''
Module to export payment orders in SEPA XML file format.

SEPA PAIN (PAyment INitiation) is the new european standard for Customer-to-Bank payment instructions. This module implements SCT (SEPA Credit Transfer), more specifically PAIN version 001.001.04.

It is part of the ISO 20022 standard, available on www.iso20022.org.

This module uses the framework provided by the banking addons, cf https://launchpad.net/banking-addons

Please contact Alexis de Lattre from Akretion <alexis.delattre@akretion.com> for any help or question about this module.
    ''',
    'active': False,
    'installable': True,
}
