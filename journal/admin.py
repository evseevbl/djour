from django.contrib import admin
from journal.models import Student, Subject, Squad, Curriculum, PersonalInfo, Penalty
# Register your models here.
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Squad)
admin.site.register(Curriculum)
admin.site.register(PersonalInfo)
admin.site.register(Penalty)
