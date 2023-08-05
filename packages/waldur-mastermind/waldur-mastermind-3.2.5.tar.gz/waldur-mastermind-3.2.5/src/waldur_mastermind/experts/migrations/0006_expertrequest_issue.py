# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-14 08:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0009_offering_article_code'),
        ('experts', '0005_expert_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='expertrequest',
            name='issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='support.Issue'),
        ),
    ]
