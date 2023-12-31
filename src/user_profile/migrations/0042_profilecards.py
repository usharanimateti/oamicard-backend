# Generated by Django 4.1.3 on 2023-04-27 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0041_card_label"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProfileCards",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("data", models.JSONField()),
                (
                    "profile",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="user_profile.userprofile",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
