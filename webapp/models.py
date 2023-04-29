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
    participants = models.ManyToManyField(
        'SingleParticipant', blank=True)


class TeamTournament(Tournament):
    participants = models.ManyToManyField(
        'TeamParticipant', blank=True)


class Participant(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(
        upload_to='player_images/', blank=True, null=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class SingleParticipant(Participant):
    tournament = models.ManyToManyField(
        SingleTournament, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class TeamParticipant(Participant):
    tournament = models.ManyToManyField(TeamTournament)
    users = models.ManyToManyField(User)


class Match(models.Model):
    home_score = models.PositiveSmallIntegerField(default=0)
    away_score = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True


class SingleMatch(Match):
    tournament = models.ForeignKey(SingleTournament, on_delete=models.CASCADE)
    home_participant = models.ForeignKey(
        SingleParticipant, on_delete=models.CASCADE, related_name='home_matches', blank=True, null=True)
    away_participant = models.ForeignKey(
        SingleParticipant, on_delete=models.CASCADE, related_name='away_matches', blank=True, null=True)


class TeamMatch(Match):
    tournament = models.ForeignKey(TeamTournament, on_delete=models.CASCADE)
    home_participant = models.ForeignKey(
        TeamParticipant, on_delete=models.CASCADE, related_name='home_matches', blank=True, null=True)
    away_participant = models.ForeignKey(
        TeamParticipant, on_delete=models.CASCADE, related_name='away_matches', blank=True, null=True)
