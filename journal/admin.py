from django.contrib import admin
from journal.models import Student, Subject, Squad, Curriculum
# Register your models here.
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Squad)
admin.site.register(Curriculum)
