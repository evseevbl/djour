from django.shortcuts import render

from journal.managers.context import with_context
from journal.models import Student, Squad, Subject
from django.contrib.auth.decorators import login_required
from maintenance.helpers.named_tuple import namedtuple_wrapper
from journal.views.common import get_average_mark

tStudentRow = namedtuple_wrapper(
    'tStudentRow',
    (
        'student',
        'avg_marks',
    )
)


@login_required()
def squad_stats(request, squad_code='1701'):
    squad = Squad.objects.get(code=squad_code)
    students = Student.objects.filter(squad=squad)
    subjects = Subject.objects.filter(curriculum__squad=squad)

    return render(
        request,
        "journal/squad_stats.html",
        with_context({
            'rows': _make_rows(students, subjects),
        })
    )


def _make_rows(students, subjects):
    return [_make_row(student, subjects) for student in students]


def _make_row(student: Student, subjects: [Subject]) -> tStudentRow:
    return tStudentRow(
        student=student,
        avg_marks=[get_average_mark(student, subj) for subj in subjects]
    )
