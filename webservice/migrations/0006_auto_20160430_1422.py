# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0005_nutron_food'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutron_food',
            old_name='calorificvalue',
            new_name='calorific_value',
        ),
    ]
