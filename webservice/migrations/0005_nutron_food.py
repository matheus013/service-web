# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webservice', '0004_auto_20160430_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutron_Food',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('calorificvalue', models.IntegerField()),
                ('diabetes', models.IntegerField()),
                ('hypertension', models.IntegerField()),
                ('anemia', models.IntegerField()),
                ('high_cholesterol', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
