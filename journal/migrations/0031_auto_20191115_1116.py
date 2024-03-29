# Generated by Django 2.2.4 on 2019-11-15 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0030_auto_20191115_1113"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="exam",
            constraint=models.UniqueConstraint(
                fields=("semester", "subject", "squad"), name="max_one_per_semester"
            ),
        ),
    ]
