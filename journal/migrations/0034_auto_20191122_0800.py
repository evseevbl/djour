# Generated by Django 2.2.4 on 2019-11-22 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0033_merge_20191122_0719"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="duty",
            name="date",
        ),
        migrations.AddField(
            model_name="duty",
            name="attendance",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="journal.Attendance",
                verbose_name="Дата",
            ),
        ),
    ]
