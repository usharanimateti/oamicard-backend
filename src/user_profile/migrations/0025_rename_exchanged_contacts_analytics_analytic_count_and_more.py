# Generated by Django 4.1.3 on 2023-02-14 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0024_auto_20221229_1221"),
    ]

    operations = [
        migrations.RenameField(
            model_name="analytics",
            old_name="exchanged_contacts",
            new_name="analytic_count",
        ),
        migrations.RemoveField(
            model_name="analytics",
            name="profile_views",
        ),
        migrations.RemoveField(
            model_name="analytics",
            name="saved_contacts",
        ),
        migrations.AddField(
            model_name="analytics",
            name="analytics_type",
            field=models.CharField(
                choices=[
                    ("profile_views", "profile_views"),
                    ("saved_contacts", "saved_contacts"),
                    ("exchanged_contacts", "exchanged_contacts"),
                ],
                default=1,
                max_length=30,
            ),
            preserve_default=False,
        ),
    ]
