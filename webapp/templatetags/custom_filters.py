from django import template
from django.db.models import Q

from webapp.models import Player

register = template.Library()


@register.filter
def is_registered(tournament, player):
    """
    Returns True if the given user is already registered with a team
    for this tournament, False otherwise.
    """
    if hasattr(tournament, 'teams'):
        players = Player.objects.filter(teams__tournament=tournament)
        return players.filter(id=player.id).exists()
    else:
        return tournament.players.filter(pk=player.pk).exists()


@register.filter
def get_team_players(team):
    return ', '.join(player.name for player in team.players.all())
