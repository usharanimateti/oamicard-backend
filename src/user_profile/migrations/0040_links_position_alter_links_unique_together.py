# Generated by Django 4.1.7 on 2023-04-10 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0039_connections_company_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="links",
            name="position",
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="links",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]
