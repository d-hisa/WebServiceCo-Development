# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-17 13:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enzemi', '0004_auto_20170317_0243'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeelist',
            old_name='mail_detination',
            new_name='detination',
        ),
    ]
