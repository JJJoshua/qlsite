# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-09 01:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_username', models.CharField(max_length=50)),
                ('stu_password', models.CharField(max_length=50)),
                ('stu_email', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'ordering': ['stu_username'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'ordering': ['username'],
            },
        ),
        migrations.CreateModel(
            name='VMImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_id', models.CharField(blank=True, max_length=36, null=True)),
                ('name', models.CharField(max_length=255)),
                ('own_project', models.CharField(max_length=32, null=True)),
                ('description', models.TextField(blank=True)),
                ('status', models.CharField(default='active', max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('size', models.BigIntegerField()),
                ('min_disk', models.IntegerField(default=0)),
                ('min_ram', models.IntegerField(default=0)),
                ('is_shared', models.CharField(default='False', max_length=10, null=True)),
                ('shared_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('flavor', models.CharField(blank=True, default='m1.tiny', max_length=10, null=True)),
                ('keypair', models.CharField(blank=True, default='mykey', max_length=20, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repo_manage.User')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
