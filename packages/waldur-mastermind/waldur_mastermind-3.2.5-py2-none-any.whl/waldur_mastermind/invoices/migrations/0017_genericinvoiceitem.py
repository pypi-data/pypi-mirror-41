# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-13 08:28
from __future__ import unicode_literals

from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import waldur_core.core.fields
import waldur_mastermind.invoices.utils


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('structure', '0052_customer_subnets'),
        ('invoices', '0016_remove_daily_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='GenericInvoiceItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=7, default=0, max_digits=22, validators=[django.core.validators.MinValueValidator(Decimal('0'))])),
                ('unit', models.CharField(choices=[(b'month', 'Per month'), (b'half_month', 'Per half month'), (b'day', 'Per day'), (b'quantity', 'Quantity')], default=b'day', max_length=30)),
                ('product_code', models.CharField(blank=True, max_length=30)),
                ('article_code', models.CharField(blank=True, max_length=30)),
                ('start', models.DateTimeField(default=waldur_mastermind.invoices.utils.get_current_month_start, help_text='Date and time when item usage has started.')),
                ('end', models.DateTimeField(default=waldur_mastermind.invoices.utils.get_current_month_end, help_text='Date and time when item usage has ended.')),
                ('project_name', models.CharField(blank=True, max_length=150)),
                ('project_uuid', models.CharField(blank=True, max_length=32)),
                ('object_id', models.PositiveIntegerField(null=True)),
                ('details', waldur_core.core.fields.JSONField(blank=True, default={}, help_text='Stores data about scope')),
                ('content_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='contenttypes.ContentType')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='generic_items', to='invoices.Invoice')),
                ('project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='structure.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
