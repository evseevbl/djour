from django.shortcuts import render
from journal.models import Attendance, StudentAttendance, Student

from journal.managers.context import with_context



def attendance(request):
    f = Attendance.objects.all()

    return render(
        request,
        "journal/attendance.html",
        with_context({
            "forms": f
        })
    )



def edit_attendance(request, attendance_id):
    att: Attendance = Attendance.objects.filter(id=attendance_id)[0]
    squad_students = Student.objects.filter(squad_id=att.squad_id)
    # a0: StudentAttendance = att.students.all()[0]
    # print(a0, a0.student, a0.value)
    # a0.value = -2
    # a0.student = Student.objects.filter(squad_id=att.squad_id)[0]
    # a0.save()
    # students = Student.objects.filter(squad_id=att.squad_id)
    return render(
        request,
        "journal/attendance_edit.html",
        with_context({
            "students": squad_students,
            "statuses": att.students.all(),
        })
    )
