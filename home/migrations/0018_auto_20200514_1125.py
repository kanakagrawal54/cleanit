# Generated by Django 3.0.6 on 2020-05-14 05:55

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20200514_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drives',
            name='contributers',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='mydrives',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]
