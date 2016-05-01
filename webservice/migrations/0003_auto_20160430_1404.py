# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0002_auto_20160430_1350'),
    ]

    operations = [
        migrations.AddField(
            model_name='nutron_user',
            name='age',
            field=models.IntegerField(default=1, verbose_name=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutron_user',
            name='anemia',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutron_user',
            name='diabetes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutron_user',
            name='height',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutron_user',
            name='high_cholesterol',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutron_user',
            name='hypertension',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutron_user',
            name='level',
            field=models.IntegerField(default=1, verbose_name=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutron_user',
            name='photo',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutron_user',
            name='score',
            field=models.IntegerField(default=0, verbose_name=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='nutron_user',
            name='weight',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
