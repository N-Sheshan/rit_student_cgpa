# Generated by Django 5.0.7 on 2024-07-30 08:51

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("application", "0007_defalut_email_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="defalut_email_id",
            name="department",
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
