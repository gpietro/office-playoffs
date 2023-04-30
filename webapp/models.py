from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to='tournament_images/', blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        abstract = True

    def clean(self):
        if self.start_date > self.end_date:
            raise ValidationError('End date must be after start date')

    def __str__(self):
        return self.name


class SingleTournament(Tournament):
    players = models.ManyToManyField(
        'Player', blank=True)


class TeamTournament(Tournament):
    max_team_size = models.IntegerField(default=2)


class Participant(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(
        upload_to='player_images/', blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Player(Participant):
    tournaments = models.ManyToManyField(
        SingleTournament, blank=True)
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, unique=True, related_name='player')

    def __str__(self):
        return self.name + " (" + self.user.username + ")"


class Team(Participant):
    tournament = models.ForeignKey(
        TeamTournament, on_delete=models.CASCADE, related_name='teams')
    players = models.ManyToManyField(Player, related_name='teams')

    def __str__(self):
        return self.name + " (" + str(self.players.count()) + "/" + str(self.tournament.max_team_size) + ")"

    def clean(self):
        super().clean()
        if self.players.count() > self.tournament.max_team_size:
            raise ValidationError('Too many players in the team.')


class Match(models.Model):
    home_score = models.PositiveSmallIntegerField(default=0)
    away_score = models.PositiveSmallIntegerField(default=0)
    date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class SingleMatch(Match):
    tournament = models.ForeignKey(
        SingleTournament, on_delete=models.CASCADE, related_name='matches')
    home_participant = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='home_matches', blank=True, null=True, related_query_name='home_match')
    away_participant = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name='away_matches', blank=True, null=True, related_query_name='away_match')

    def __str__(self):
        if self.date:
            return self.home_participant.name + " vs " + self.away_participant.name + " - " + str(self.home_score) + ":" + str(self.away_score)
        else:
            return self.home_participant.name + " vs " + self.away_participant.name + " - " + "not played yet"


class TeamMatch(Match):
    tournament = models.ForeignKey(
        TeamTournament, on_delete=models.CASCADE, related_name='matches')
    home_participant = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='home_matches', blank=True, null=True, related_query_name='home_match')
    away_participant = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='away_matches', blank=True, null=True, related_query_name='away_match')

    def __str__(self):
        if self.date:
            return self.home_participant.name + " vs " + self.away_participant.name + " - " + str(self.home_score) + ":" + str(self.away_score)
        else:
            return self.home_participant.name + " vs " + self.away_participant.name + " - " + "not played yet"
