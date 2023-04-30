import logging
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from webapp.forms import CreateSingleMatchForm, CreateTeamMatchForm

from webapp.models import SingleMatch, Player, SingleTournament, TeamMatch, Team, TeamTournament

logger = logging.getLogger(__name__)


def index(request):
    context = {
        'user': request.user,
    }
    return render(request, 'webapp/index.html', context)


@login_required
def profile(request):
    user = request.user
    player = Player.objects.filter(user=user).first()
    single_tournaments = SingleTournament.objects.all()
    team_tournaments = TeamTournament.objects.all()
    context = {
        'player': player,
        'single_tournaments': single_tournaments,
        'team_tournaments': team_tournaments,
    }
    return render(request, 'webapp/profile.html', context)


@login_required
def tournament_teams(request, tournament_id):
    tournament = get_object_or_404(TeamTournament, pk=tournament_id)
    teams = tournament.teams.all()
    player = Player.objects.get(user=request.user)

    context = {
        'tournament': tournament,
        'teams': teams,
        'player': player,
    }
    return render(request, 'webapp/tournament_teams.html', context)


@login_required
def join_single_tournament(request, tournament_id):
    tournament = get_object_or_404(SingleTournament, pk=tournament_id)
    player = Player.objects.get(user=request.user)
    # Check if the user is already registered for the tournament
    if tournament.players.filter(pk=player.pk).exists():
        logger.warn('User is already registered for this tournament.')
        return redirect('single_tournament_detail', tournament_id=tournament.id)

    tournament.players.add(player)
    tournament.save()
    logger.info('You have successfully registered for this tournament.')
    return redirect('single_tournament_detail', tournament_id=tournament.id)


@login_required
def single_tournament_detail(request, tournament_id):
    tournament = get_object_or_404(SingleTournament, pk=tournament_id)
    participants = tournament.players.all()
    matches = SingleMatch.objects.filter(tournament=tournament)

    player_points = {}
    for player in participants:
        player_points[player] = 0

    for match in matches:
        if match.home_score > match.away_score:
            player_points[match.home_participant] = player_points.get(
                match.home_participant, 0) + 3
        elif match.home_score < match.away_score:
            player_points[match.away_participant] = player_points.get(
                match.away_participant, 0) + 3
        elif match.date:
            player_points[match.home_participant] = player_points.get(
                match.home_participant, 0) + 1
            player_points[match.away_participant] = player_points.get(
                match.away_participant, 0) + 1

    sorted_players = sorted(player_points.items(),
                            key=lambda x: x[1], reverse=True)

    context = {
        'tournament': tournament,
        'participants': participants,
        'matches': matches,
        'sorted_players': sorted_players,
    }
    return render(request, 'webapp/single_tournament_detail.html', context)


@login_required
def team_tournament_detail(request, tournament_id):
    tournament = get_object_or_404(TeamTournament, pk=tournament_id)
    teams = tournament.teams.all()
    matches = TeamMatch.objects.filter(tournament=tournament)

    team_points = {}
    for team in teams:
        team_points[team] = 0

    for match in matches:
        if match.home_score > match.away_score:
            team_points[match.home_participant] = team_points.get(
                match.home_participant, 0) + 3
        elif match.home_score < match.away_score:
            team_points[match.away_participant] = team_points.get(
                match.away_participant, 0) + 3
        elif match.date:
            team_points[match.home_participant] = team_points.get(
                match.home_participant, 0) + 1
            team_points[match.away_participant] = team_points.get(
                match.away_participant, 0) + 1

    sorted_teams = sorted(team_points.items(),
                          key=lambda x: x[1], reverse=True)

    context = {
        'tournament': tournament,
        'teams': teams,
        'matches': matches,
        'sorted_teams': sorted_teams
    }
    return render(request, 'webapp/team_tournament_detail.html', context)


@login_required
def create_team_view(request, tournament_id):
    tournament = get_object_or_404(TeamTournament, pk=tournament_id)

    if request.method == 'POST':
        player = get_object_or_404(Player, user=request.user)
        team_name = request.POST['team_name']

        if player.teams.filter(tournament=tournament).exists():
            messages.error(
                request, 'You have already have a team for this tournament.')
            return redirect('tournament_teams', tournament_id=tournament_id)

        else:
            team = Team.objects.create(
                name=team_name,
                tournament=tournament,
            )
            team.players.add(player)
            team.save()

            return redirect('tournament_teams', tournament_id=tournament_id)

    else:
        return render(request, 'webapp/create_team.html', {'tournament': tournament})


@login_required
def join_team_view(request, team_id):
    if request.method == 'POST':
        team = get_object_or_404(Team, pk=team_id)
        player = get_object_or_404(Player, user=request.user)
        team.players.add(player)
        messages.success(request, 'You have successfully joined the team.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

    return HttpResponse(status=400)


@login_required
def create_single_match(request, tournament_id):
    tournament = get_object_or_404(SingleTournament, pk=tournament_id)
    players = tournament.players.all()
    if request.method == 'POST':
        form = CreateSingleMatchForm(request.POST)

        if form.is_valid():
            match = form.save(commit=False)
            match.tournament = tournament
            match.save()
            form.save_m2m()
            return redirect('single_tournament_detail', tournament_id=tournament.id)
    else:
        form = CreateSingleMatchForm()

    return render(request, 'webapp/create_single_match.html', {'form': form, 'tournament': tournament, 'players': players})


@login_required
def create_team_match(request, tournament_id):
    tournament = get_object_or_404(TeamTournament, pk=tournament_id)
    teams = tournament.teams.all()
    if request.method == 'POST':
        form = CreateTeamMatchForm(request.POST)

        if form.is_valid():
            match = form.save(commit=False)
            match.tournament = tournament
            match.save()
            form.save_m2m()
            return redirect('team_tournament_detail', tournament_id=tournament.id)
    else:
        form = CreateTeamMatchForm()

    return render(request, 'webapp/create_team_match.html', {'form': form, 'tournament': tournament, 'teams': teams})
