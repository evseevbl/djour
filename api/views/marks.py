import json

from django.http import HttpResponse

from api.models import rMark
from journal.models import Mark



def add_mark(request):
    m = Mark()
    d = json.loads(request.body)
    print(d)
    req = rMark(
        value=d["value"],
        id=d["mark_id"],
        student_id=d["student_id"],
        # subject_id=d["subject_id"],
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
            # subject_id=req.subject_id,
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


