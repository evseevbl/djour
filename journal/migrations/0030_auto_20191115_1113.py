# Generated by Django 2.2.4 on 2019-11-15 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0029_exam_squad"),
    ]

    operations = [
        migrations.RenameField(
            model_name="exam",
            old_name="cemester",
            new_name="semester",
        ),
        migrations.AddField(
            model_name="exam",
            name="name",
            field=models.CharField(
                choices=[("exam", "Экзамен"), ("test", "Зачёт")],
                default="",
                max_length=100,
                verbose_name="Форма контроля",
            ),
        ),
    ]
