# Generated by Django 4.1.7 on 2023-02-28 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0036_card_card_serial_no"),
    ]

    operations = [
        migrations.AddField(
            model_name="card",
            name="assigned",
            field=models.BooleanField(default=False),
        ),
    ]
