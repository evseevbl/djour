# Generated by Django 2.2.4 on 2019-12-11 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0038_auto_20191211_0721"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="event",
            options={
                "managed": True,
                "verbose_name": "Мероприятие",
                "verbose_name_plural": "Мероприятия",
            },
        ),
        migrations.AlterModelOptions(
            name="eventparticipant",
            options={
                "managed": True,
                "verbose_name": "Участник мероприятия",
                "verbose_name_plural": "Участники мероприятия",
            },
        ),
        migrations.AlterField(
            model_name="student",
            name="pic",
            field=models.ImageField(blank=True, null=True, upload_to="students_pic/"),
        ),
    ]
