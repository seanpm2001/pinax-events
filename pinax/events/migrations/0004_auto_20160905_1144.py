# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-05 11:44
from __future__ import unicode_literals

from django.db import migrations, models
import pinax.events.models


class Migration(migrations.Migration):

    dependencies = [
        ('pinax_events', '0003_event_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='secondary_image',
            field=models.ImageField(blank=True, upload_to=pinax.events.models.image_upload_to),
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, upload_to=pinax.events.models.image_upload_to),
        ),
    ]