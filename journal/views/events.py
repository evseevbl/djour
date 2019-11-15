from django.shortcuts import render

from journal.managers.context import with_context


from django.contrib.auth.decorators import login_required

@login_required()
def event(request):
    return render(
        request,
        "journal/index.html",
        with_context({})
    )