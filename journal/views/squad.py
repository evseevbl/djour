from django.shortcuts import render

from journal.managers.context import with_context
from journal.models import Student, Squad, Subject
from django.contrib.auth.decorators import login_required
from maintenance.helpers.named_tuple import namedtuple_wrapper
from journal.views.common import avg_mark_student, avg_marks_group
from django.db.models import QuerySet

tStudentRow = namedtuple_wrapper(
    'tStudentRow',
    (
        'student',
        'avg_marks',
    )
)

tUnitRow = namedtuple_wrapper(
    'tUnitRow',
    (
        'unit',
        'rows',
        'subtotal',
    )
)


@login_required()
def squad_stats(request, squad_code='1701'):
    squad = Squad.objects.get(code=squad_code)
    students = Student.objects.filter(squad=squad).order_by('unit', 'last_name')
    subjects = Subject.objects.filter(curriculum__squad=squad)

    return render(
        request,
        "journal/squad_stats.html",
        with_context({
            'subjects': subjects,
            'unit_rows': _make_unit_rows(students, subjects),
            'total': _make_squad_total(students, subjects),
        })
    )

def _make_squad_total(students, subjects):
    return tStudentRow(
        avg_marks=[avg_marks_group(students, subj) for subj in subjects]
    )

def _make_unit_rows(students: QuerySet, subjects):
    ls = []
    for (u, _) in Student.UNIT_CHOICES:
        unit_students = students.filter(unit=u)
        rows = _make_rows(unit_students, subjects)
        # total = _make_subtotal(unit_students, subjects)
        total = list(range(7))
        ls.append(tUnitRow(
            rows=rows,
            unit=u,
            subtotal=_make_subtotal(unit_students, subjects),
        ))
    return ls


def _make_subtotal(students, subjects):
    return tStudentRow(
        # student=student,
        avg_marks=[avg_marks_group(students, subj) for subj in subjects]
    )

def _make_rows(students, subjects):
    return [_make_row(student, subjects) for student in students]


def _make_row(student: Student, subjects: [Subject]) -> tStudentRow:
    return tStudentRow(
        student=student,
        avg_marks=[avg_mark_student(subj, student.id) for subj in subjects]
    )
