# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timezone_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_remove_coinzauruser_income_period'),
    ]

    operations = [
        migrations.RenameField(
            model_name='expense',
            old_name='user',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='user',
            new_name='author',
        ),
        migrations.AlterField(
            model_name='coinzauruser',
            name='timezone',
            field=timezone_field.fields.TimeZoneField(default=b'Europe/Warsaw'),
        ),
    ]
