from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from journal.models import Mark, Lesson, Squad
from api.forms import LessonForm
from maintenance.helpers.named_tuple import namedtuple_wrapper
import json
import datetime as dt

rMark = namedtuple_wrapper(
    "requestMark",
    [
        "value",
        "id",
        "student_id",
        "subject_id",
        "teacher_id",
        "lesson_id",
    ]
)

rLesson = namedtuple_wrapper(
    "requestLesson",
    [
        "name",
        "date",
        "subject_id",
        "squad_id",
    ]
)



def add_mark(request):
    m = Mark()
    d = json.loads(request.body)
    print(d)
    req = rMark(
        value=d["value"],
        id=d["mark_id"],
        student_id=d["student_id"],
        subject_id=d["subject_id"],
        teacher_id=1,  # ToDo
        lesson_id=d["lesson_id"]
    )

    if req.id:
        print("mark exists")
        m: Mark = Mark.objects.filter(id=req.id)[0]
        if req.value != '':
            m.val = req.value
            m.save()
        else:
            m.delete()
    else:
        print("new mark")
        m = Mark(
            student_id=req.student_id,
            subject_id=req.subject_id,
            teacher_id=req.teacher_id,
            val=req.value,
            lesson_id=req.lesson_id
        )
        m.save()

    data = {
        "id": m.id,
    }
    print(m)
    return HttpResponse(json.dumps(data))



def add_lesson(request):
    print(request)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LessonForm(request.POST)
        data = form.data
        squad = Squad.objects.filter(code=data["squad_code"])[0]
        # print("form=", form.data['date'], form.data['name'])
        print("form=", form.data)
        l = Lesson(
            name=data["name"],
            subject_id=data["subject_id"],
            squad=squad,
            date=dt.datetime.strptime(data["date"], '%d-%m-%Y')
        )
        l.save()

        print(request.build_absolute_uri())  # Keeps query parameters

        print(request.get_full_path())  # Keeps query parameters
    # return HttpResponseRedirect("")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
