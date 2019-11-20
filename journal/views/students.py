from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from journal.managers.context import with_context
from journal.models import Student, Mark, Subject, StudentAttendance, PersonalInfo, Penalty, Attendance
from journal.managers.marks import tAvg
from django.db.models import Avg, Case, When

from datetime import datetime as dt
from django.views.decorators.csrf import ensure_csrf_cookie
from maintenance.helpers.named_tuple import namedtuple_wrapper

tPenaltyOption = namedtuple_wrapper(
    'tPenaltyOption',
    (
        'code',
        'label'
    )
)

tPenaltiesGot = namedtuple_wrapper(
    'tPenaltiesGot',
    (
        'label',
        'got'
    )
)


@ensure_csrf_cookie
@login_required
def students(request):
    ls: [Student] = Student.objects.all()
    return render(
        request,
        "journal/students.html",
        with_context({
            # "user_id": user_id,
            "students": ls,
        })
    )


@ensure_csrf_cookie
@login_required
def student(request, student_id):
    st: Student = Student.objects.filter(id=student_id).first()
    all_subjects = Subject.objects.filter(curriculum__squad=st.squad)
    avgs = []
    for subj in all_subjects:
        avgs.append(tAvg(
            short=subj.short,
            avg=get_avg_for_subject(subj, student_id)
        ))
        # todo оценки с учётом пропусков
        # avgs.append(tAvg(
        #     short=subj.short + ' (с пропусками)',
        #     avg=get_avg_for_subject(subj, student_id, absent_zero=True)
        # ))
    atts = StudentAttendance.objects.filter(student=st)
    stats = {
        "absent": 0,
        "truant": 0,
        "duty": 0,
        "present": 0,
    }
    for a in atts:
        a: StudentAttendance = a
        stats[a.value] += 1

    info = PersonalInfo.objects.filter(student=st).first()

    all_attendances = Attendance.objects.filter(squad=st.squad)

    penalties = Penalty.objects.filter(student=st)

    penalties_got_map = {'Кол-во взысканий': 0, 'Кол-во поощрений': 0}
    choices = {'reprimand': 'Кол-во взысканий', 'promotion': 'Кол-во поощрений'}

    penalty_options = []
    for code, label in Penalty.CHOICES:
        penalty_options.append(tPenaltyOption(code=code, label=label))

    for penalty in penalties:
        penalties_got_map[choices[penalty.type]] += 1

    penalties_got = []
    for key, value in penalties_got_map.items():
        penalties_got.append(tPenaltiesGot(label=key, got=value))

    return render(
        request,
        "journal/student.html",
        with_context({
            "student": st,
            "avg_marks": avgs,
            "attendance": stats,
            "info": info,
            "penalties": penalties,
            "penalty_options": penalty_options,
            "penalties_got": penalties_got,
            "all_attendances": all_attendances
        })
    )


def get_avg_for_subject(subject, student_id, absent_zero=False):
    print("avg for", subject.short)
    if absent_zero:
        marks = Mark.objects.filter(student_id=student_id, lesson__subject=subject)
    else:
        marks = Mark.objects.filter(student_id=student_id, lesson__subject=subject, val__gt=0)
    avg, cnt = 0, 0
    # todo разобраться с Avg и Case/When
    for m in marks:
        m: Mark = m
        if m.val < 0:
            m.val = 0
        avg += m.val
        cnt += 1
    if cnt > 0:
        avg /= cnt
    else:
        avg = None
    print(f'avg student={student_id}, avg={avg}, subj={subject.short}, zeroed={absent_zero}')
    return avg
