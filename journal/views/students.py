from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from journal.managers.context import with_context
from journal.models import Student, Mark, Subject, Lesson, StudentAttendance, PersonalInfo, Curriculum
from journal.managers.marks import tAvg
from django.db.models import Avg

from django.views.decorators.csrf import ensure_csrf_cookie



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



@login_required
@ensure_csrf_cookie
def student(request, student_id):
    st: Student = Student.objects.filter(id=student_id).first()
    all_subjects = Subject.objects.filter(curriculum__squad=st.squad)
    avgs = []
    for subj in all_subjects:
        avgs.append(tAvg(
            short=subj.short,
            avg=get_avg_for_subject(subj, student_id)
        ))
        avgs.append(tAvg(
            short=subj.short + ' (с пропусками)',
            avg=get_avg_for_subject(subj, student_id, absent_zero=True)
        ))
    atts = StudentAttendance.objects.filter(student=st)
    stats = {
        "absent": 0,
        "truant": 0,
        "duty": 0,
        "present": 0,
    }
    for a in atts:
        print("a=", a, a.value, a.student.last_name)
        a: StudentAttendance = a
        stats[a.value] += 1
    print(stats)

    info = PersonalInfo.objects.filter(student=st).first()

    return render(
        request,
        "journal/marks/student.html",
        with_context({
            "student": st,
            "avg_marks": avgs,
            "attendance": stats,
            "info": info,
        })
    )



def get_avg_for_subject(subject, student_id, absent_zero=False):
    print("avg for", subject.short)
    marks = []
    if absent_zero:
        marks = Mark.objects.filter(student_id=student_id).filter(lesson__subject=subject)
    else:
        marks = Mark.objects.filter(val__gt=0).filter(student_id=student_id).filter(lesson__subject=subject)

    for m in marks:
        m: Mark = m
        if m.val < 0:
            m.val = 0
        # print(m.id, m.lesson.subject.short, m.val)
    avg = marks.aggregate(Avg('val'))
    ret = avg['val__avg']
    print(f'avg student={student_id}, avg={ret}, subj={subject.short}, zeroed={absent_zero}')
    return ret
