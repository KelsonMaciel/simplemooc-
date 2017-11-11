# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-07 02:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0013_auto_20171022_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='material',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='lessons/materials'),
        ),
        migrations.AlterField(
            model_name='material',
            name='lesson',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='courses.Lesson', verbose_name='Aula'),
        ),
    ]
