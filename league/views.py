# Developed by S309918
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Club, Profile


@login_required(login_url='/login/')
def home(request):
    all_clubs = Club.objects.all()
    return render(request, 'league/home.html', {'all_clubs': all_clubs})


@login_required(login_url='/login/')
def assign_favourite_club(request):
    if request.method == 'POST':
        club_id = request.POST.get('club_id')
        selected_club = Club.objects.get(id=club_id)

        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.favourite_club = selected_club
        profile.save()

        return redirect('home')

    clubs = Club.objects.all()
    return render(request, 'league/assign_favourite.html', {'clubs': clubs})


class UserLoginView(LoginView):
    template_name = 'league/login.html'
    next_page = 'home'