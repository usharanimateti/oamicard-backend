# Generated by Django 4.1.7 on 2023-02-24 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0006_request"),
    ]

    operations = [
        migrations.AddField(
            model_name="request",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default="2023-02-24 12:49:03.000 +0530"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="request",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
