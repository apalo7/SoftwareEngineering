from django.contrib import admin

from league.models import Club, Player, Match, ClubSeasonStat, Profile

# Register your models here.

admin.site.register(Club)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(ClubSeasonStat)
admin.site.register(Profile)
