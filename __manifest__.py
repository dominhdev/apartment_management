# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Viproperty Base',
    'version': '2.0',
    'summary': "Management Base config of Viproperty.",
    'author': 'Viproperty JSC',
    'price': '1000.0',
    'currency': 'USD',
    'depends': [
        'base',
        'property_management',
        'property_landlord_management',
        'property_maintenance',
        'om_account_asset',
        'maintenance',
        'sales_team',
        'hr',
        'crm',
        'om_account_asset',
        'product',
        'multiple_property_rent', 'board', 'web_responsive'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/res_groups.xml',
        'data/ir_config_parameter.xml',
        'views/res_groups_view.xml',
        'views/res_users_view.xml',
        'views/profile_group_history_view.xml',
        'wizard/change_profile_group_view.xml',
        'views/menu.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
    'installable': True,
    'auto_install': False,
    'images': ['static/description/icon.png']
}
