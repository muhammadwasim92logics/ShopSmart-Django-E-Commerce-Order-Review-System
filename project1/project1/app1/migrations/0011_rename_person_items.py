# Generated by Django 5.1.7 on 2025-03-24 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_rename_ice_customers_ice_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Person',
            new_name='Items',
        ),
    ]
