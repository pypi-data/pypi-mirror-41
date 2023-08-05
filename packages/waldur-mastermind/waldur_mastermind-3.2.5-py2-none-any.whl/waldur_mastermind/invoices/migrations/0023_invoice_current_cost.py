# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-19 08:47
from __future__ import unicode_literals

from django.db import migrations, models


def migrate_data(apps, schema_editor):
    Invoice = apps.get_model('invoices', 'Invoice')

    for invoice in Invoice.objects.all():
        invoice.update_current_cost()


class Migration(migrations.Migration):

    dependencies = [
        ('invoices', '0022_remove_payment_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='current_cost',
            field=models.DecimalField(decimal_places=2, default=0, editable=False, help_text='Cached value for current cost.', max_digits=10),
        ),
        migrations.RunPython(migrate_data, reverse_code=migrations.RunPython.noop),
    ]
