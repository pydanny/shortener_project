# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LinkLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('http_accept_language', models.TextField(verbose_name='HTTP_ACCEPT_LANGUAGE', blank=True)),
                ('http_host', models.CharField(max_length=255, verbose_name='HTTP_HOST', blank=True)),
                ('http_referer', models.CharField(max_length=255, verbose_name='HTTP_REFERER', blank=True)),
                ('http_user_agent', models.CharField(max_length=255, verbose_name='HTTP_USER_AGENT', blank=True)),
                ('query_string', models.TextField(verbose_name='QUERY_STRING', blank=True)),
                ('remote_addr', models.CharField(max_length=255, verbose_name='REMOTE_ADDR', blank=True)),
                ('remote_host', models.CharField(max_length=255, verbose_name='REMOTE_HOST', blank=True)),
                ('request_method', models.CharField(max_length=30, verbose_name='REQUEST_METHOD', blank=True)),
                ('link', models.ForeignKey(to='links.Link')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
