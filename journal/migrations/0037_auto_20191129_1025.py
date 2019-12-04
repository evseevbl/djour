# Generated by Django 2.2.6 on 2019-11-29 10:25

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0036_student_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('pic', '300x300', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
        migrations.AlterField(
            model_name='student',
            name='pic',
            field=models.ImageField(null=True, upload_to='students_pic/'),
        ),
    ]