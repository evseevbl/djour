from django.shortcuts import render
from journal.models import Student, Squad, Mark
from journal.manager import by_subject, students_to_keys, make_cells, tKey, tMark, get_squads_with_subjects



# Create your views here.
def index(request):
    name = "boris"
    if request.GET.get('mybtn'):
        name = str(request.GET.get('mytextbox'))

    return render(
        request,
        "journal/index.html",
        {
            "user": name
        }
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
        {
            # "user_id": user_id,
            "students": ls,
        }
    )



def student(request, student_id):
    ls: [Student] = Student.objects.filter(id=student_id)
    return render(
        request,
        "journal/marks/student.html",
        {
            # "user_id": user_id,
            "student": ls[0],
        }
    )



def test(request):
    return render(request, "journal/index.html")



def marks_base(request):
    marks = Mark.objects.all()
    return render(
        request,
        "journal/marks/base.html",
        {
            "marks": marks
        }
    )



def marks_squad(request, squad_code="1702"):
    keys = students_to_keys(Student.objects.filter(squad__code=squad_code))
    marks_list = Mark.objects.filter(student__squad__code=squad_code).prefetch_related(
        'student__mark_set',
        'student__squad__student_set',
    )
    x_keys = [
        tKey(id=1, display="7.09", sort=1),
        tKey(id=2, display="14.09", sort=2),
        tKey(id=3, display="21.09", sort=3),
    ]

    y_keys = [
        tKey(id=1, display="Пупкин В.В", sort=1),
        tKey(id=2, display="Шлюпкин И.С", sort=2),
    ]

    marks = [
        tMark(
            id=123,
            x_key=1,
            y_key=1,
            val=5
        ),
        tMark(
            id=124,
            x_key=3,
            y_key=2,
            val=3
        ),
    ]
    header, cells = make_cells(x_keys, y_keys, marks)
    q = get_squads_with_subjects()
    print(q)
    # cells = make_cells()
    return render(
        request,
        "journal/marks/marks_squad.html",
        {
            "header": header,
            "cells": cells,
            "marks": marks,
            "squad_list": q,
        }
    )
