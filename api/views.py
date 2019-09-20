from django.shortcuts import render
from django.http import HttpResponse
from journal.models import Mark
from maintenance.helpers.named_tuple import namedtuple_wrapper
import json

rMark = namedtuple_wrapper(
    "requestMark",
    [
        "value",
        "id",
        "subject_id",
        "teacher_id",

    ]
)



# Create your views here.
def add_mark(request):
    d = json.loads(request.body)
    req = rMark(
        value=d["value"],
        id=d["mark_id"],
        subject_id=d["subject_id"],
        teacher_id=1,  # ToDo
        # date=d["date"]
    )
    if req.id:
        print("mark exists")
        m: Mark = Mark.objects.filter(id=req.id)[0]
        m.val = req.value
        m.save()
    else:
        print("new mark")
        # m = Mark(
        #     student_id=req.student_id,
        # subject_id=req.stud["subject_id"],
        #     val=d["value"]
        # )

    print(m)
    return HttpResponse("OK")
