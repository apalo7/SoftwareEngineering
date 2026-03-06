from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
]

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='league/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('assign-favourite/', views.assign_favourite, name='assign_favourite'),
    path('matches/', views.match_results, name='match_results'),
    path('standings/', views.league_standings, name='standings'),
    path('clubs/', views.club_list, name='club_list'),
    path('players/', views.player_list, name='player_list'),
    path('transfer/', views.transfer_center, name='transfer_center'),
]