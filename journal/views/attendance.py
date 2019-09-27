from django.shortcuts import render

from journal.managers.context import with_context



def attendance(request):
    return render(
        request,
        "journal/attendance.html",
        with_context({
        })
    )
