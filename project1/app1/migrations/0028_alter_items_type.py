# Generated by Django 5.1.6 on 2025-04-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app1", "0027_card_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="items",
            name="type",
            field=models.CharField(
                choices=[
                    ("Chocolate", "Chocolate"),
                    ("Mango ", "Mango"),
                    ("Strawberry", "Strawberry"),
                    ("Vanilla", "Vanilla"),
                    ("Salted Caramel", "Salted Caramel"),
                    ("Mint Chocolate Chip", "Mint Chocolate Chip"),
                    ("Pineapple Coconu ", "Pineapple Coconu"),
                    ("Cookies & Cream ", "Cookies & Cream"),
                    ("Blue Barry", "Blue Barry"),
                ],
                max_length=22,
            ),
        ),
    ]
