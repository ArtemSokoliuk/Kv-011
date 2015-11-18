# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plan_editor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='floor',
            old_name='image',
            new_name='plan',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='coordinate',
            new_name='coordinates',
        ),
        migrations.RenameField(
            model_name='workplace',
            old_name='coordinate',
            new_name='coordinates',
        ),
        migrations.RemoveField(
            model_name='office',
            name='city',
        ),
        migrations.RemoveField(
            model_name='office',
            name='country',
        ),
        migrations.AddField(
            model_name='office',
            name='address',
            field=models.CharField(max_length=100, default=None),
            preserve_default=False,
        ),
    ]
