# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-17 13:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enzemi', '0006_auto_20170317_1335'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeelist',
            old_name='employee_name',
            new_name='name',
        ),
    ]
