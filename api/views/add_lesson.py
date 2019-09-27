import datetime as dt

from django.http import HttpResponseRedirect

from api.forms import LessonForm
from journal.models import Squad, Lesson



def add_lesson(request):
    print(request)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LessonForm(request.POST)
        data = form.data
        squad = Squad.objects.filter(code=data["squad_code"])[0]
        # print("form=", form.data['date'], form.data['name'])
        print("form=", form.data)
        lesson = Lesson(
            name=data["name"],
            subject_id=data["subject_id"],
            squad=squad,
            date=dt.datetime.strptime(data["date"], '%d-%m-%Y')
        )
        lesson.save()

        print(request.build_absolute_uri())  # Keeps query parameters

        print(request.get_full_path())  # Keeps query parameters
    # return HttpResponseRedirect("")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))