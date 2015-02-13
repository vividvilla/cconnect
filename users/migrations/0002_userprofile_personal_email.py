# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='personal_email',
            field=models.EmailField(max_length=224, null=True, blank=True),
            preserve_default=True,
        ),
    ]
