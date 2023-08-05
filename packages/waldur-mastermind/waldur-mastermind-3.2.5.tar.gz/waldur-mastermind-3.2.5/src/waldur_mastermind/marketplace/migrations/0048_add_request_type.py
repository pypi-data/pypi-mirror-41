# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-23 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0047_rewire_order_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Create'), (2, 'Update'), (3, 'Terminate')], default=1),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Create'), (2, 'Update'), (3, 'Terminate')], default=1),
        ),
    ]
