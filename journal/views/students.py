from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from journal.managers.context import with_context
from journal.models import Student, Mark, Subject

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



@login_required
@ensure_csrf_cookie
def student(request, student_id):
    st: [Student] = Student.objects.filter(id=student_id).first()

    subjs = Subject.objects.filter(lesson__mark__student_id=student_id).prefetch_related('lesson_set')
    print(subjs)
    for s in subjs:
        get_avg_for_subject(s, student_id)


    return render(
        request,
        "journal/marks/student.html",
        with_context({
            # "user_id": user_id,
            "student": st,
        })
    )



def get_avg_for_subject(subject, student_id):
    marks = Mark.objects.filter(lesson__subject=subject, student_id=student_id).prefetch_related('student__mark_set__lesson', 'lesson__subject')
    for m in marks:
        m: Mark = m
        print(m.val, m.student_id)
    pass
