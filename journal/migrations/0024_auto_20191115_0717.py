# Generated by Django 2.2.4 on 2019-11-15 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0023_examattempt_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exam',
            options={'managed': True, 'verbose_name': 'Форма контроля', 'verbose_name_plural': 'Формы контроля'},
        ),
        migrations.AlterModelOptions(
            name='examattempt',
            options={'managed': True, 'verbose_name': 'Попытка сдачи экзамена', 'verbose_name_plural': 'Попытки сдачи экзамена'},
        ),
        migrations.AlterModelOptions(
            name='exammark',
            options={'managed': True, 'verbose_name': 'Оценка за форму контроля', 'verbose_name_plural': 'Оценки за форму контроля'},
        ),
    ]