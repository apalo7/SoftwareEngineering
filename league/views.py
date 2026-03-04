from django.shortcuts import render

from league.models import Clubs


# Create your views here.

def home(request):
    clubs = Clubs.objects.all()
    return render(request, 'league/home.html', {'clubs': clubs})