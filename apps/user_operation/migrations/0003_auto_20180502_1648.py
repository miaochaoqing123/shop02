# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-02 08:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_operation', '0002_auto_20180502_1611'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Useraddresss',
            new_name='UserAddress',
        ),
        migrations.RenameModel(
            old_name='UserleavingMesage',
            new_name='UserLeavingMessage',
        ),
    ]
