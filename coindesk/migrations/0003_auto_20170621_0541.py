# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-21 05:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coindesk', '0002_auto_20170617_2343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='payment_req',
            new_name='payment_request',
        ),
    ]
