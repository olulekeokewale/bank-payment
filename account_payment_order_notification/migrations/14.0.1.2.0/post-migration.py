# Copyright 2022 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.load_data(
        env.cr,
        "account_payment_order_notification",
        "migrations/14.0.1.2.0/noupdate_changes.xml",
    )
    openupgrade.delete_record_translations(
        env.cr,
        "account_payment_order_notification",
        ["email_account_payment_order_notification"],
    )
