# Generated by Django 2.2.4 on 2019-11-15 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0031_auto_20191115_1116"),
    ]

    operations = [
        migrations.AddField(
            model_name="lesson",
            name="exam",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="journal.Exam",
                verbose_name="Экзамен",
            ),
        ),
    ]
