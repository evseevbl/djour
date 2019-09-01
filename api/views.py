from journal.models import Squad
from django.shortcuts import render_to_response



# Create your views here.
def get_squads(request):
    squads = Squad.objects.all()
    return render_to_response('select/item.html',
                              {'squads': squads})
