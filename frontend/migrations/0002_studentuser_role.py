# Generated by Django 5.2.3 on 2025-06-14 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentuser",
            name="role",
            field=models.CharField(
                choices=[("admin", "Admin"), ("user", "User")],
                default="user",
                max_length=10,
            ),
        ),
    ]
