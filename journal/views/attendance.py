from django.shortcuts import render

from journal.managers.context import with_context



def attendance(request):
    name = "boris"
    if request.GET.get('mybtn'):
        name = str(request.GET.get('mytextbox'))

    return render(
        request,
        "journal/attendance.html",
        with_context({
            "user": name
        })
    )
