# Generated by Django 4.1.3 on 2022-12-16 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0002_userprofile_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="address",
            name="profile",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_profile.userprofile",
            ),
        ),
        migrations.AlterField(
            model_name="contactinformation",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="user_profile.userprofile",
            ),
        ),
        migrations.AlterField(
            model_name="links",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="user_profile.userprofile",
            ),
        ),
        migrations.AlterField(
            model_name="video",
            name="profile",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="user_profile.userprofile",
            ),
        ),
    ]