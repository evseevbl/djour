import datetime as dt

from django.http import HttpResponseRedirect
import json

from api.forms import PenaltyForm
from journal.models import Penalty, Student, Attendance


def add_penalty(request):
    if request.method == 'POST':
        attrs = request.POST
        if len(request.POST) == 0:
            attrs = json.loads(request.body)
        form = PenaltyForm(attrs)
        print(form.errors)
        data = form.data
        print("form=", data)
        student = Student.objects.filter(pk=data['student_id'])[0]
        attendance = Attendance.objects.get(date=data['date'], squad=student.squad)
        penalty = Penalty(
            type=data['penalty_type'],
            comment=data['comment'],
            student=student,
            attendance=attendance,
            date=dt.datetime.strptime(data['date'], '%Y-%m-%d'),
        )
        penalty.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def get_student_penalties(request):
    if request.method == 'GET':
        pass
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
