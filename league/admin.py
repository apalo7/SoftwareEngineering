from django.contrib import admin

from league.models import Clubs, Players, Matches, ClubSeasonStats, Profile

# Register your models here.

admin.site.register(Clubs)
admin.site.register(Players)
admin.site.register(Matches)
admin.site.register(ClubSeasonStats)
admin.site.register(Profile)
