# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0003_auto_20160430_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutron_user',
            name='age',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nutron_user',
            name='level',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='nutron_user',
            name='score',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
