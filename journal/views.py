from django.shortcuts import render
from journal.models import Student, Squad, Mark, Subject
from journal.managers.marks import tMark, tKey, by_subject, make_cells, students_to_keys
from journal.managers.context import with_context
from django.views.decorators.csrf import ensure_csrf_cookie



# Create your views here.
def index(request):
    name = "boris"
    if request.GET.get('mybtn'):
        name = str(request.GET.get('mytextbox'))

    return render(
        request,
        "journal/index.html",
        with_context({
            "user": name
        })
    )



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



def test(request):
    return render(request, "journal/index.html")



def marks_base(request):
    marks = Mark.objects.all()
    return render(
        request,
        # "journal/marks/marks_squad.html",
        with_context({
            "marks": marks
        })
    )

@ensure_csrf_cookie
def marks_squad(request, squad_code="1702", subject_id=1):
    subj = Subject.objects.filter(id=subject_id)[0]
    y_keys = students_to_keys(Student.objects.filter(squad__code=squad_code))
    marks_list = Mark.objects.filter(student__squad__code=squad_code).prefetch_related(
        'student__mark_set',
        'student__squad__student_set',
    ).filter(subject_id=subject_id)
    x_keys = [
        tKey(id=1, display="7.09", sort=1, val=1),
        tKey(id=2, display="14.09", sort=2, val=2),
        tKey(id=3, display="21.09", sort=3, val=3),
    ]

    # y_keys = [
    #     tKey(id=1, display="Пупкин В.В", sort=1),
    #     tKey(id=2, display="Шлюпкин И.С", sort=2),
    # ]

    marks = [
        tMark(
            id=72,
            x_key=1,
            y_key=8,
            val=5
        ),
        tMark(
            id=73,
            x_key=2,
            y_key=13,
            val=3
        ),
    ]
    header, cells = make_cells(x_keys, y_keys, marks)
    # cells = make_cells()
    return render(
        request,
        "journal/marks/marks_squad.html",
        with_context({
            "header": header,
            "cells": cells,
            "marks": marks,
            "subject": subj,
            "x_keys": x_keys,
            "y_keys": y_keys,
            "subject_id": subject_id,
        })
    )
