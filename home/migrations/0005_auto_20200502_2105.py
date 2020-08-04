# Generated by Django 3.0.4 on 2020-05-02 15:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_drives'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drives',
            name='Place',
        ),
        migrations.AddField(
            model_name='drives',
            name='contributers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=' ', max_length=100), null=True, size=50),
        ),
        migrations.AddField(
            model_name='drives',
            name='creator',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='drives',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='drives',
            name='place',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='my_drives',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(default=' ', max_length=100), null=True, size=50),
        ),
        migrations.AlterField(
            model_name='drives',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profession',
            field=models.CharField(max_length=100, null=True),
        ),
    ]