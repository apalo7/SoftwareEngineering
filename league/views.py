from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from .models import Club, Profile, Match, Player


@login_required(login_url='/login/')
def home(request):
    all_clubs = Club.objects.all()
    return render(request, 'league/home.html', {'all_clubs': all_clubs})


from .models import Club, Profile

@login_required(login_url='/login/')
def assign_favourite(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    all_club = Club.objects.all()

    if request.method == 'POST':
        club_id = request.POST.get('club_id')
        if club_id:
            selected_club = Club.objects.get(id=club_id)
            profile.favourite_club.clear()
            profile.favourite_club.add(selected_club)
            return redirect('home')

    return render(request, 'league/assign_favourite.html', {'all_club': all_club})

@login_required(login_url='/login/')
def match_results(request):
    matches = Match.objects.all().order_by('-match_date')
    return render(request, 'league/match_results.html', {'matches': matches})

@login_required(login_url='/login/')
def league_standings(request):
    all_club = Club.objects.all()
    return render(request, 'league/standings.html', {'all_club': all_club})

@login_required(login_url='/login/')
def club_list(request):
    all_club = Club.objects.all()
    return render(request, 'league/clubs.html', {'all_club': all_club})

@login_required(login_url='/login/')
def player_list(request):
    all_player = Player.objects.all()
    return render(request, 'league/players.html', {'all_player': all_player})


@login_required(login_url='/login/')
def transfer_center(request):
    if not request.user.is_superuser:
        return redirect('home')

    all_player = Player.objects.all()
    all_club = Club.objects.all()

    if request.method == 'POST':
        player_id = request.POST.get('player_id')
        new_club_id = request.POST.get('new_club_id')

        if player_id and new_club_id:
            player = Player.objects.get(id=player_id)
            new_club = Club.objects.get(id=new_club_id)

            player.club = new_club
            player.save()
            return redirect('player_list')  # Transfer sonrası listeye atar

    return render(request, 'league/transfer_center.html', {
        'all_player': all_player,
        'all_club': all_club
    })

class UserLoginView(LoginView):
    template_name = 'league/login.html'
    next_page = 'home'