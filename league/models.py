from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Club(models.Model):
    club_name = models.CharField(max_length=100)
    foundation_year = models.IntegerField()
    club_colours = models.CharField(max_length=100)
    coach_name = models.CharField(max_length=100)

    def __str__(self):
        return self.club_name


class Player(models.Model):
    club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='players')
    player_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    position = models.CharField(max_length=100)
    market_value = models.BigIntegerField()

    def __str__(self):
        return self.player_name

class Match(models.Model):
    home_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='home_matches')
    away_club = models.ForeignKey(Club, on_delete=models.CASCADE, related_name='away_matches')
    match_date = models.DateField()
    home_score = models.IntegerField()
    away_score = models.IntegerField()

    def __str__(self):
        return f'{self.home_club} {self.home_score} - {self.away_club} {self.away_score}'


class ClubSeasonStat(models.Model):
    club = models.OneToOneField(Club, on_delete=models.CASCADE)
    matches_played = models.IntegerField()
    wins = models.IntegerField()
    draws = models.IntegerField()
    losses = models.IntegerField()
    goals_scored = models.IntegerField()
    goals_against = models.IntegerField()
    goal_difference = models.IntegerField()
    points = models.IntegerField()

    def __str__(self):
        return f"{self.club.club_name} Stats"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favourite_club = models.ManyToManyField(Club, blank=True)

    def __str__(self):
        return self.user.username
