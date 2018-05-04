# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-03 23:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_goodscategorybrand_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goodscategory',
            old_name='it_tab',
            new_name='is_tab',
        ),
        migrations.RemoveField(
            model_name='goodsimage',
            name='image_url',
        ),
        migrations.AlterField(
            model_name='goods',
            name='goods_front_images',
            field=models.ImageField(blank=True, null=True, upload_to='goods/images/', verbose_name='封面图片'),
        ),
        migrations.AlterField(
            model_name='goodscategorybrand',
            name='image',
            field=models.ImageField(max_length=200, upload_to='brands/'),
        ),
    ]
