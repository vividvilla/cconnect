# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20150213_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone',
            field=models.CharField(max_length=10),
            preserve_default=True,
        ),
    ]
