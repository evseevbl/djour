from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from journal.managers.context import with_context
from journal.models import Student, Mark, Subject, StudentAttendance, PersonalInfo, Penalty, Attendance, Exam, Duty
from journal.managers.marks import tAvg
from django.db.models import Avg, Case, When

from datetime import datetime as dt
from django.views.decorators.csrf import ensure_csrf_cookie
from maintenance.helpers.named_tuple import namedtuple_wrapper

tOption = namedtuple_wrapper(
    'tOption',
    (
        'code',
        'label'
    )
)

tCount = namedtuple_wrapper(
    'tCount',
    (
        'label',
        'count'
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
            avg=_get_avg_for_subject(subj, student_id),
            # exams=
        ))
        # todo оценки с учётом пропусков
        # avgs.append(tAvg(
        #     short=subj.short + ' (с пропусками)',
        #     avg=get_avg_for_subject(subj, student_id, absent_zero=True)
        # ))

    atts = StudentAttendance.objects.filter(student=st)

    info = PersonalInfo.objects.filter(student=st).first()

    all_attendances = Attendance.objects.filter(squad=st.squad)

    penalties = Penalty.objects.filter(student=st)

    penalty_choices = {
        Penalty.REPRIMAND: 'Взысканий',
        Penalty.PROMOTION: 'Поощрений',
    }
    penalties_got_map = {penalty_choices[Penalty.PROMOTION]: 0, penalty_choices[Penalty.REPRIMAND]: 0}

    for penalty in penalties:
        penalties_got_map[penalty_choices[penalty.type]] += 1

    penalty_stats = []
    for key, value in penalties_got_map.items():
        penalty_stats.append(tCount(label=key, count=value))

    duties = Duty.objects.filter(student=st)

    return render(
        request,
        "journal/student.html",
        with_context({
            "student": st,
            "avg_marks": avgs,
            "attendance_stats": _get_attendance_stats(atts),
            "info": info,
            "penalties": penalties,
            "penalty_options": _get_options(Penalty.CHOICES),
            "penalty_stats": penalty_stats,
            "all_attendances": all_attendances,
            # "all_exams": _get_exam_marks(student),
            "duty_options": _get_options(Duty.CHOICES),
            "duty_stats": _get_avg_duty_marks(st),
            "duties": duties
        })
    )


def _get_penalties():
    pass


def _get_options(model_choices):
    opts = []
    for code, label in model_choices:
        opts.append(tOption(code=code, label=label))
    return opts


def _get_exam_marks(st: Student) -> [Exam]:
    exams = Exam.objects.filter(squad=st.squad)
    return exams


def _get_attendance_stats(atts: [StudentAttendance]) -> dict:
    stats = {
        "absent": 0,
        "truant": 0,
        "duty": 0,
        "present": 0,
    }
    for a in atts:
        a: StudentAttendance = a
        stats[a.value] += 1
    return stats


def _get_avg_for_subject(subject, student_id, absent_zero=False):
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

def _get_avg_duty_marks(st_obj):
    duties_choices = {
        Duty.DETENTION: 'Выходы в наряд',
        Duty.DUTY: 'Дежурства',
    }
    avgs = {duties_choices[Duty.DETENTION]: 0, duties_choices[Duty.DUTY]: 0}

    duties = Duty.objects.filter(student=st_obj)

    for type, label in duties_choices.items():
        duties_by_type = duties.filter(type=type)
        if not duties_by_type:
            avgs[label] = '-'
            pass
        for duty in duties_by_type:
            avgs[label] += duty.mark
        avgs[label] /= duties_by_type.count()

    return avgs
