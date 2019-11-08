import datetime as dt

from django.http import HttpResponseRedirect

from api.forms import LessonForm
from journal.models import Squad, Lesson, StudentAttendance, Mark



def add_penalty(request):
    print(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
