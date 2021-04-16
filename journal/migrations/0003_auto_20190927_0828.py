# Generated by Django 2.2.4 on 2019-09-27 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0002_remove_squad_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student",
            options={
                "managed": True,
                "verbose_name": "Студент",
                "verbose_name_plural": "Студенты",
            },
        ),
        migrations.AlterModelOptions(
            name="subject",
            options={
                "managed": True,
                "verbose_name": "Дисциплина",
                "verbose_name_plural": "Дисциплины",
            },
        ),
        migrations.RemoveField(
            model_name="mark",
            name="subject",
        ),
    ]
