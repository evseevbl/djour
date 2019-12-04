from django.shortcuts import render
from journal.models import Event
from journal.managers.context import with_context


def events(request):
    f = Event.objects.all().order_by('-date')

    return render(
        request,
        'journal/events.html',
        {'forms': f, }
    )
