# Generated by Django 4.1.3 on 2022-12-19 05:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0010_alter_links_provider_alter_links_url_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="analytics",
            old_name="user_profile_id",
            new_name="profile",
        ),
        migrations.RenameField(
            model_name="connections",
            old_name="connection_profile_id",
            new_name="connection_profile",
        ),
        migrations.RenameField(
            model_name="connections",
            old_name="user_profile_id",
            new_name="profile",
        ),
        migrations.RenameField(
            model_name="shareddetails",
            old_name="profile_id",
            new_name="profile",
        ),
        migrations.RenameField(
            model_name="usersettings",
            old_name="user_id",
            new_name="user",
        ),
    ]
