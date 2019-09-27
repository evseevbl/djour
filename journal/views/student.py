from django.shortcuts import render

from journal.managers.context import with_context
from journal.models import Student



from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import ensure_csrf_cookie



@login_required
@ensure_csrf_cookie
def student(request, student_id):
    ls: [Student] = Student.objects.filter(id=student_id)
    return render(
        request,
        "journal/marks/student.html",
        with_context({
            # "user_id": user_id,
            "student": ls[0],
        })
    )