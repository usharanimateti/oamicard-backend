# Generated by Django 4.1.3 on 2022-12-29 12:21

import os
import shutil
from pathlib import Path

from django.db import migrations

provider_icon_path = "./provider_icons"


def insert_providers(apps, schema_editor):
    provider_model = apps.get_model("user_profile", "Providers")
    folder_path = Path.cwd() / "media/icons"
    for filename in os.listdir(provider_icon_path):
        file_path = os.path.join(provider_icon_path, filename)

        if os.path.isfile(file_path):
            shutil.copy2(file_path, folder_path)
            provider_obj = provider_model.objects.filter(
                title=os.path.splitext(filename)[0].title()
            ).first()
            if not provider_obj:
                provider_model.objects.create(
                    icon="icons/" + filename,
                    title=os.path.splitext(filename)[0].title(),
                )
            else:
                provider_obj.icon = "icons/" + filename
                provider_obj.save()


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ("user_profile", "0023_alter_video_profile"),
    ]

    operations = [
        migrations.RunPython(insert_providers, reverse_code=migrations.RunPython.noop),
    ]
