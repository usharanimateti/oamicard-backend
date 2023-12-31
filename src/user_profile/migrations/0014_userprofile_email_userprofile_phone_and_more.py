# Generated by Django 4.1.3 on 2022-12-20 09:26

import django.db.models.deletion
from django.db import migrations, models

import user_profile.validators


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0013_alter_video_video_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="email",
            field=models.JSONField(
                default=list, validators=[user_profile.validators.validate_email]
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="phone",
            field=models.JSONField(
                default=list, validators=[user_profile.validators.validate_phone]
            ),
        ),
        migrations.AddField(
            model_name="userprofile",
            name="website",
            field=models.JSONField(
                default=list, validators=[user_profile.validators.validate_website]
            ),
        ),
        migrations.AlterField(
            model_name="links",
            name="provider",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="user_profile.providers",
            ),
        ),
        migrations.DeleteModel(
            name="ContactInformation",
        ),
    ]
