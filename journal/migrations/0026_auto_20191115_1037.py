# Generated by Django 2.2.4 on 2019-11-15 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0025_remove_mark_teacher'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exammark',
            name='attempt',
        ),
        migrations.RemoveField(
            model_name='exammark',
            name='student',
        ),
        migrations.DeleteModel(
            name='ExamAttempt',
        ),
        migrations.DeleteModel(
            name='ExamMark',
        ),
    ]