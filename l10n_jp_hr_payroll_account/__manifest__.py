# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Japanese - Payroll with Accounting',
    'category': 'Localization',
    'depends': ['l10n_jp_hr_payroll', 'hr_payroll_account', 'l10n_jp'],
    'description': """
Accounting Data for Japanese Payroll Rules.
=============================================   
    * Expense Encoding
    * Payment Encoding
    * Company Contribution Management
    """,

    'auto_install': True,
    'author': 'gudo_soft',
    'website': 'http://gudo-soft.world.coocan.jp',
    'data':[
        'data/l10n_jp_hr_payroll_account_data.xml',
    ],
    'post_init_hook': '_set_accounts',
}
