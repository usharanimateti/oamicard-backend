# Generated by Django 4.1.3 on 2023-01-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0004_invitationcode_first_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="invitationcode",
            name="first_name",
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
