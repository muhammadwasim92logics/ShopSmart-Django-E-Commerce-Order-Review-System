# Generated by Django 5.1.6 on 2025-03-21 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='avalible_ch',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='person',
            name='dec',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='person',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
