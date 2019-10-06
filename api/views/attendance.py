import datetime as dt

from django.http import HttpResponseRedirect

from api.forms import NewAttendanceForm
from journal.models import Squad, Lesson, Attendance, Student, StudentAttendance



def add_attendance(request):
    if request.method == 'POST':
        form = NewAttendanceForm(request.POST)
        squad_code = form.data["squad_code"]
        date = form.data["date"]

        squad = Squad.objects.filter(code=squad_code)[0]
        att = Attendance(
            date=dt.datetime.strptime(date, '%d-%m-%Y'),
            squad=squad,
        )
        att.save()

        students = Student.objects.filter(squad_id=squad.id)
        for student in students:
            val = StudentAttendance(
                value=-1,
                student=student
            )
            val.save()
            att.students.add(val)
            pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
