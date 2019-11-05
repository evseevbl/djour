# Generated by Django 2.2.4 on 2019-11-01 12:25

from django.db import migrations, models



class Migration(migrations.Migration):
    dependencies = [
        ('journal', '0010_auto_20191101_0804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lesson',
            options={'managed': True, 'verbose_name': 'Занятие', 'verbose_name_plural': 'Занятия'},
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='duty',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='exam',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='final',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='finalmark',
            name='val',
            field=models.IntegerField(blank=True, null=True, verbose_name='Оценка'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='name',
            field=models.CharField(blank=True, max_length=100, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='comment',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Комментарий'),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='date',
            field=models.DateField(verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Полное название'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='short',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Сокращённое название'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Имя'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Фамилия'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Отчество'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='rank',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='звание'),
        ),
    ]