# Generated by Django 2.2.8 on 2019-12-20 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0042_auto_20191220_0805"),
    ]

    operations = [
        migrations.AddField(
            model_name="userextension",
            name="date_limit",
            field=models.BooleanField(default=False),
        ),
    ]
