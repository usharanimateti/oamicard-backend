# Generated by Django 4.1.3 on 2023-02-14 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "user_profile",
            "0025_rename_exchanged_contacts_analytics_analytic_count_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="analytics",
            name="analytic_count",
        ),
    ]
