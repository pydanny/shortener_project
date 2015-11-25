# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields
import links.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('original_url', models.CharField(unique=True, max_length=255, verbose_name='URL to be shortened')),
                ('identifier', models.CharField(blank=True, max_length=100, verbose_name='Identifier', db_index=True, validators=[links.validators.validate_five_characters])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
