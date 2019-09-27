from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from journal.managers.context import with_context
from journal.models import Student

from django.views.decorators.csrf import ensure_csrf_cookie



@ensure_csrf_cookie
@login_required
def students(request):
    # manager = StudentsManager()
    # students = manager.get_students_by_squad('1702')
    # q = Student.objects.filter(squad=Squad(code='1702'))
    ls: [Student] = Student.objects.all()
    # squad__code="1702")
    # # filter(squad='1702')
    return render(
        request,
        "journal/students.html",
        with_context({
            # "user_id": user_id,
            "students": ls,
        })
    )
