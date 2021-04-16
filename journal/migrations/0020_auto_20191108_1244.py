# Generated by Django 2.2.4 on 2019-11-08 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("journal", "0019_auto_20191108_1239"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="penalty",
            options={
                "managed": True,
                "verbose_name": "Взыскание/поощрение",
                "verbose_name_plural": "Взыскания и поощрения",
            },
        ),
        migrations.AlterField(
            model_name="penalty",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="journal.Student"
            ),
        ),
        migrations.AlterField(
            model_name="penalty",
            name="type",
            field=models.CharField(
                choices=[("reprimand", "взыскание"), ("promotion", "поощрение")],
                default="reprimand",
                max_length=20,
                verbose_name="Вид",
            ),
        ),
    ]
