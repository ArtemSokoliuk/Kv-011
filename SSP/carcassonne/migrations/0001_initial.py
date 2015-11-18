# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_pg.models.fields.json


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to='')),
                ('number', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coordinate', django_pg.models.fields.json.JSONField(null=True, blank=True, default=None)),
                ('number', models.IntegerField()),
                ('floor', models.ForeignKey(to='plan_editor.Floor')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Workplace',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('coordinate', django_pg.models.fields.json.JSONField(null=True, blank=True, default=None)),
                ('number', models.IntegerField()),
                ('status', models.BooleanField()),
                ('room', models.ForeignKey(to='plan_editor.Room')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='floor',
            name='office',
            field=models.ForeignKey(to='plan_editor.Office'),
        ),
    ]
