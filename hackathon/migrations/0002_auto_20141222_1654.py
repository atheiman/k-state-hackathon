# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hackathon', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entrant',
            name='team',
            field=models.ForeignKey(blank=True, to='hackathon.Team', null=True),
            preserve_default=True,
        ),
    ]
