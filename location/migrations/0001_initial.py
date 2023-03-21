# Generated by Django 3.2 on 2023-03-21 17:08

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='title')),
                ('points', django.contrib.postgres.fields.jsonb.JSONField(verbose_name='points')),
            ],
            options={
                'verbose_name': 'location',
                'verbose_name_plural': 'locations',
            },
        ),
    ]
