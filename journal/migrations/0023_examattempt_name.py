# Generated by Django 2.2.4 on 2019-11-15 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0022_exams_20191115_0702"),
    ]

    operations = [
        migrations.AddField(
            model_name="examattempt",
            name="name",
            field=models.CharField(
                blank=True, max_length=100, null=True, verbose_name="Название"
            ),
        ),
    ]
