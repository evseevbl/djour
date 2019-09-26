from django.shortcuts import render

from journal.managers.context import with_context
from journal.models import Mark



def marks_base(request):
    marks = Mark.objects.all()
    return render(
        request,
        # "journal/marks/marks_squad.html",
        with_context({
            "marks": marks
        })
    )