import datetime as dt

from django.http import HttpResponseRedirect

from api.forms import NewAttendanceForm, SetAttendanceStatusForm
from journal.models import Squad, Lesson, Attendance, Student, StudentAttendance, StudentAttendanceType
from journal.constants import *



def add_attendance(request):
    if request.method == 'POST':
        form = NewAttendanceForm(request.POST)
        squad_code = form.data["squad_code"]
        date = form.data["date"]
        # todo constants
        present = StudentAttendanceType.objects.get(value="present")

        squad = Squad.objects.filter(code=squad_code)[0]
        att = Attendance(
            date=dt.datetime.strptime(date, '%d-%m-%Y'),
            squad=squad,
        )
        att.save()

        students = Student.objects.filter(squad_id=squad.id)
        for student in students:
            val = StudentAttendance(
                student=student,
                type=present,
            )
            val.save()
            att.students.add(val)
            pass

    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))



def set_attendance(request):
    if request.method == 'POST':
        form = SetAttendanceStatusForm(request.POST)
        data = form.data
        student_id = data["student_id"]
        att_id = data["attendance_id"]
        att_type_id = data["attendance_type"]

        att_type = StudentAttendanceType.objects.filter(id=att_type_id).first()
        att = Attendance.objects.filter(id=att_id).first()

        student_att: StudentAttendance = StudentAttendance.objects.filter(student_id=student_id, attendance=att).first()
        student_att.type = att_type
        student_att.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
