from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from journal.managers.context import with_context
from journal.managers.marks import students_to_keys, tKey, tMark, make_cells
from journal.models import Subject, Mark, Lesson, Student



@login_required
@ensure_csrf_cookie
def marks_squad(request, squad_code="1702", subject_id=1):
    subj = Subject.objects.filter(id=subject_id)[0]
    marks_list = Mark.objects.filter(student__squad__code=squad_code).prefetch_related(
        'student__mark_set',
        'student__squad__student_set',
    ).filter(subject_id=subject_id)
    # x_keys = [
    #     tKey(id=1, display="7.09", sort=1, val=dt.date(2019, 9, 7).isoformat()),
    #     tKey(id=2, display="14.09", sort=2, val=2),
    #     tKey(id=3, display="21.09", sort=3, val=3),
    # ]
    lessons: [Lesson] = Lesson.objects.filter(squad__code='1701')
    print(lessons)

    # y_keys = [
    #     tKey(id=1, display="Пупкин В.В", sort=1),
    #     tKey(id=2, display="Шлюпкин И.С", sort=2),
    # ]
    y_keys = students_to_keys(Student.objects.filter(squad__code=squad_code))
    x_keys = [
        tKey(
            id=l.id,
            display=l.date.strftime("%d.%m"),
            sort=l.date,
            val=l.id,
            comment=l.name,
        ) for l in lessons
    ]
    allMarks = Mark.objects.filter(student__squad__code=squad_code, subject_id=subject_id)
    print(allMarks)
    c = marks_to_keys(allMarks)
    print(c)
    marks = c
    # marks = [
    #     tMark(
    #         id=72,
    #         x_key=1,
    #         y_key=2,
    #         val=5
    #     ),
    #     tMark(
    #         id=73,
    #         x_key=2,
    #         y_key=1,
    #         val=3
    #     ),
    # ]
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



def marks_to_keys(all_marks: [Mark]) -> [tMark]:
    return [
        tMark(
            id=m.id,
            x_key=m.lesson_id,
            y_key=m.student_id,
            val=m.val,
        ) for m in all_marks
    ]
