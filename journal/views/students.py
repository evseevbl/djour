from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from journal.managers.context import with_context
from journal.models import Student, Mark, Subject, Lesson
from journal.managers.marks import tAvg
from django.db.models import Avg

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

    lessons = (Lesson.objects.filter(mark__student=st))
    subjs = set()
    for l in lessons:
        l: Lesson = l
        subjs.add(l.subject_id)
        # print("s", l.subject.short)
    print(subjs)
    avgs = []
    for s in subjs:
        subj = Subject.objects.filter(id=s).first()
        avgs.append(tAvg(
            short=subj.short,
            avg=get_avg_for_subject(subj, student_id)
        ))

    return render(
        request,
        "journal/marks/student.html",
        with_context({
            "student": st,
            "avg_marks": avgs,
        })
    )



def get_avg_for_subject(subject, student_id):
    print("avg for", subject.short)
    marks = Mark.objects.filter(val__gt=0).filter(student_id=student_id).filter(lesson__subject=subject)

    for m in marks:
        m: Mark = m
        print(m.id, m.lesson.subject.short, m.val)
    avg = marks.aggregate(Avg('val'))
    return avg['val__avg']
