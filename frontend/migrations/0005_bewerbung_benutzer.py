# Generated by Django 5.2.3 on 2025-06-16 22:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("frontend", "0004_bewerbung_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="bewerbung",
            name="benutzer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="bewerbungen",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
