# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-03-17 02:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enzemi', '0003_auto_20170307_1916'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeelist',
            old_name='t01_author',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='employeelist',
            old_name='t01_create_time',
            new_name='create_time',
        ),
        migrations.RenameField(
            model_name='employeelist',
            old_name='t01_update_time',
            new_name='update_time',
        ),
        migrations.RenameField(
            model_name='employeelist',
            old_name='t01_updater',
            new_name='updater',
        ),
        migrations.AlterModelTable(
            name='nighttaskmaster',
            table='night_task_master',
        ),
    ]
