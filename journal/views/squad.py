from django.shortcuts import render

from journal.managers.context import with_context
from journal.models import *
from django.contrib.auth.decorators import login_required
from maintenance.helpers.named_tuple import namedtuple_wrapper
from journal.views.common import avg_mark_student, avg_marks_group, get_attendance_stats, students_to_ids
from django.db.models import QuerySet


tStudentRow = namedtuple_wrapper(
    'tStudentRow',
    (
        'student',
        'avg_marks',
        'attendance'
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

tSubjectMark = namedtuple_wrapper(
    'tSubjectMark',
    (
        'semester',
        'mark',
    )
)

tSubjectAvgs = namedtuple_wrapper(
    'tSubjectAvgs',
    (
        'subject',
        'avgs',
    )
)

tUnitAvgs = namedtuple_wrapper(
    'tUnitAvgs',
    (
        'num',
        'val',
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
            'units': _get_units_marks(students, subjects),
        })
    )


def _get_units_marks(students, subjects):
    result = []
    for i in range(1, 4):
        unit_students = students.filter(unit=i).all()
        result.append(tUnitAvgs(num=i, val=_get_unit_marks(subjects, unit_students)))
    return result


def _extract_exam_marks(ls: Lesson, st: Student):
    mark = Mark.objects.filter(lesson=ls, student=st).filter(val__in=[1,2,3,4,5]).first()
    print(mark)
    if mark is None:
        return 0
    return mark.val

def _lessons_to_ids(lessons:[Lesson]):
    return [l.id for l in lessons]


def _get_unit_marks(subjects, students):
    result = []
    for subj in subjects:
        all_marks = {}
        for st in students:
            exams = Exam.objects.filter(squad=st.squad)
            needed_exams = exams.filter(subject=subj)
            for e in needed_exams:
                # lesson = Lesson.objects.filter(exam=e).order_by('-attendance__date').first()
                lessons = Lesson.objects.filter(exam=e)
                mark = Mark.objects.filter(lesson_id__in=_lessons_to_ids(lessons), val__gt=0, student=st).order_by('-lesson__attendance__date').first()
                mark = mark.val
                # ffmark = _extract_exam_marks(lesson, st)
                if mark != 0:
                    if e.semester in all_marks.keys():
                        all_marks[e.semester][0] += mark
                        all_marks[e.semester][1] += 1
                    else:
                        all_marks[e.semester] = [mark, 1]
        avgs = [tSubjectMark(semester=item[0],
                             mark=round(item[1][0]/item[1][1], 2))
                for item in all_marks.items()]
        result.append(tSubjectAvgs(subject=subj.short, avgs=avgs))
    return result


def _make_squad_total(students, subjects):
    return tStudentRow(
        avg_marks=[avg_marks_group(students, subj) for subj in subjects],
        attendance=get_attendance_stats(StudentAttendance.objects.filter(student_id__in=students_to_ids(students))),
    )

def _make_unit_rows(students: QuerySet, subjects):
    ls = []
    for (u, _) in Student.UNIT_CHOICES:
        unit_students = students.filter(unit=u)
        rows = _make_rows(unit_students, subjects)
        # total = _make_subtotal(unit_students, subjects)
        ls.append(tUnitRow(
            rows=rows,
            unit=u,
            subtotal=_make_subtotal(unit_students, subjects),
        ))
    return ls


def _make_subtotal(students, subjects):
    return tStudentRow(
        # student=student,
        avg_marks=[avg_marks_group(students, subj) for subj in subjects],
        attendance=get_attendance_stats(StudentAttendance.objects.filter(student_id__in=students_to_ids(students))),
    )

def _make_rows(students, subjects):
    return [_make_row(student, subjects) for student in students]


def _make_row(student: Student, subjects: [Subject]) -> tStudentRow:
    return tStudentRow(
        student=student,
        avg_marks=[avg_mark_student(subj, student.id) for subj in subjects],
        attendance=get_attendance_stats(StudentAttendance.objects.filter(student=student)),
    )
