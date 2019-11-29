from django.contrib import admin
from journal.models import *
from image_cropping import ImageCroppingMixin


class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass


# Register your models here.
admin.site.register(Subject)
admin.site.register(Student, MyModelAdmin)
admin.site.register(Squad)
admin.site.register(Curriculum)
admin.site.register(PersonalInfo)
admin.site.register(Penalty)
admin.site.register(Exam)
admin.site.register(Attendance)
admin.site.register(Lesson)
