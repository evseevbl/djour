from django.shortcuts import render
from journal.models import Attendance, StudentAttendance, Student, StudentAttendanceType

from journal.managers.context import with_context



def attendance(request):
    f = Attendance.objects.all()

    return render(
        request,
        "journal/attendance.html",
        with_context({
            "forms": f,
        })
    )



def edit_attendance(request, attendance_id):
    att: Attendance = Attendance.objects.filter(id=attendance_id)[0]
    # squad_students = Student.objects.filter(squad_id=att.squad_id)
    types = StudentAttendanceType.objects.all()
    # squad_students = att.students.all()
    return render(
        request,
        "journal/attendance_edit.html",
        with_context({
            "students": att.students.all().order_by('student__last_name').prefetch_related('student'),
            "statuses": att.students.all(),
            "attendance_types": types,
            "attendance_id": attendance_id,
            "squad_code": att.squad.code,
            "date": att.date,
        })
    )
