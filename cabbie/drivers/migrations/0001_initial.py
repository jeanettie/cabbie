# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-21 20:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=1)),
                ('mentor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drivers.Driver')),
            ],
        ),
        migrations.AddField(
            model_name='description',
            name='drivers',
            field=models.ManyToManyField(related_name='descriptions', to='drivers.Driver'),
        ),
    ]
