# Generated by Django 5.1.7 on 2025-03-24 16:55

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_icecreamimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='type',
            field=models.CharField(choices=[('C-Ice', 'Chocolate'), ('M-Ice', 'Mango'), ('S-Ice', 'Strawberry'), ('W-Ice', 'Vanilla'), ('salted', 'Salted Caramel'), ('Mint', 'Mint Chocolate Chip'), ('Pineapple ', 'Pineapple Coconu'), ('cookies ', 'Cookies & Cream'), ('Blue Barry', 'Blue Barry')], max_length=14),
        ),
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=12)),
                ('address', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('ice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customers', to='app1.person')),
            ],
        ),
    ]
