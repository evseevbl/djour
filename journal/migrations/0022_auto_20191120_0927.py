# Generated by Django 2.2.4 on 2019-11-20 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0021_auto_20191113_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='duty',
            name='type',
            field=models.CharField(choices=[('duty', 'дежурство'), ('detention', 'наряд')], default='duty', max_length=20, verbose_name='Вид'),
        ),
        migrations.DeleteModel(
            name='DutyType',
        ),
    ]