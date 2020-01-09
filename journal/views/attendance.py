from django.shortcuts import render
from journal.models import Attendance, UserExtension
from maintenance.helpers.named_tuple import namedtuple_wrapper
from journal import constants
from journal.managers.context import with_context
from datetime import date

tNewAttendance = namedtuple_wrapper(
    'tNewAttendance',
    (
        'date',
        'squad',
    )
)



def attendance(request):
    restrictions = None
    try:
        ext = UserExtension.objects.get(user=request.user)
    except UserExtension.DoesNotExist:
        ext = None
    if ext:
        allowed_squads = ext.squads.all()
        f = Attendance.objects.filter(squad__in=allowed_squads)
        restrictions = [
            tNewAttendance(
                date=date.today(),
                squad=squad,
            ) for squad in allowed_squads]
    else:
        # all forms, no restrictions
        f = Attendance.objects.all()

    return render(
        request,
        "journal/attendance.html",
        with_context({
            "forms": f,
            "restrictions": restrictions
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
