# Generated by Django 4.1.3 on 2022-12-16 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_profile", "0008_alter_address_profile_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="profile_picture",
            field=models.ImageField(upload_to="media"),
        ),
    ]