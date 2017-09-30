# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 16:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the company', max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Company',
                'ordering': ['name'],
                'verbose_name_plural': 'Companies',
            },
        ),
        migrations.CreateModel(
            name='CompanyAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(help_text='Street of the address', max_length=255, verbose_name='Street')),
                ('postcode', models.CharField(blank=True, default='', help_text='Post code of the address (if applicable)', max_length=255, null=True, verbose_name='Post code')),
                ('locality', models.CharField(blank=True, help_text='Locality of the address, e.g. village, city', max_length=255, null=True, verbose_name='Locality')),
                ('region', models.CharField(blank=True, help_text='Region of the address, e.g. state, province, county', max_length=255, null=True, verbose_name='Region')),
                ('country', models.CharField(blank=True, help_text='Country of the address, e.g. nation state', max_length=255, null=True, verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Company Address',
                'ordering': ['street'],
                'verbose_name_plural': 'Company Addresses',
            },
        ),
        migrations.CreateModel(
            name='ConstructionSystem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the construction system', max_length=255, verbose_name='Name')),
                ('component_id', models.CharField(blank=True, help_text='Component ID of the construction system', max_length=255, null=True, verbose_name='Component ID')),
                ('certification_date', models.DateField(blank=True, help_text='When the construction system was certified', null=True, verbose_name='Certification Date')),
                ('description_de', models.TextField(blank=True, help_text='German description of the construction system', null=True, verbose_name='Description (de)')),
                ('description_en', models.TextField(blank=True, help_text='English description of the construction system', null=True, verbose_name='Description (en)')),
                ('total_thickness', models.FloatField(blank=True, help_text='Total thickness of the construction system in m', null=True, verbose_name='Total Thickness')),
                ('u_value', models.FloatField(blank=True, help_text='Thermal transmittance of the construction system in W/(m2K)', null=True, verbose_name='U-Value')),
            ],
            options={
                'verbose_name': 'Construction System',
                'ordering': ['name', 'certification_date'],
                'verbose_name_plural': 'Construction Systems',
            },
        ),
        migrations.CreateModel(
            name='ConstructionSystemCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the category', max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Construction System Category',
                'ordering': ['name'],
                'verbose_name_plural': 'Construction System Categories',
            },
        ),
        migrations.AddField(
            model_name='constructionsystem',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Category of the construction system', null=True, on_delete=django.db.models.deletion.SET_NULL, to='construction_systems.ConstructionSystemCategory', verbose_name='Category'),
        ),
        migrations.AddField(
            model_name='company',
            name='address',
            field=models.ForeignKey(blank=True, help_text='Address of the company', null=True, on_delete=django.db.models.deletion.SET_NULL, to='construction_systems.CompanyAddress', verbose_name='Address'),
        ),
    ]