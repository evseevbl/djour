import json

from django.http import HttpResponse

from api.models import rMark
from journal.models import Mark


def add_mark(request):
    value2marks = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        'п': -1,
        'у': -2,
        'н': -3,
    }
    m = Mark()
    d = json.loads(request.body)
    print(d)
    req = rMark(
        value=value2marks.get(d["value"].lower()),
        id=d["mark_id"],
        student_id=d["student_id"],
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
            # subject_id=req.subject_id,
            # teacher_id=req.teacher_id,
            val=req.value,
            lesson_id=req.lesson_id
        )
        m.save()

    data = {
        "id": m.id,
    }
    print(m)
    return HttpResponse(json.dumps(data))
