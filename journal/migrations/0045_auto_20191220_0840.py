# Generated by Django 2.2.8 on 2019-12-20 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0044_auto_20191220_0838"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userextension",
            name="squads",
            field=models.ManyToManyField(
                blank=True,
                to="journal.Squad",
                verbose_name="Может редактировать взвода",
            ),
        ),
    ]
