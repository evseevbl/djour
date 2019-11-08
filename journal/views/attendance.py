from django.shortcuts import render
from journal.models import Attendance
from journal import constants
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
    types = constants.ATT_TYPES

    return render(
        request,
        "journal/attendance_edit.html",
        with_context({
            "students": att.students.all().order_by('student__last_name').prefetch_related('student'),
            "statuses": att.students.all().order_by('student__last_name').prefetch_related('student'),
            "attendance_types": types,
            "attendance_id": attendance_id,
            "squad_code": att.squad.code,
            "date": att.date,
        })
    )
