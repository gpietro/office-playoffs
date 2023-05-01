from django.urls import path
from . import views

urlpatterns = [
    path('accounts/profile/', views.profile, name='profile'),
    # single tournament
    path('single-tournaments/<int:tournament_id>/join/',
         views.join_single_tournament, name='single_tournament_join'),
    path('single-tournaments/<int:tournament_id>/matches/new/',
         views.create_single_match, name='single_tournament_create_match'),
    path('single-tournaments/<int:tournament_id>/matches/<int:pk>/edit/',
         views.SingleMatchEditView.as_view(), name='single_tournament_edit_match'),
    path('single-tournaments/<int:tournament_id>/',
         views.single_tournament_detail, name='single_tournament_detail'),

    # team tournament
    path('team-tournaments/<int:tournament_id>/teams/new/',
         views.create_team_view, name='team_tournament_create_team'),
    path('team-tournaments/<int:tournament_id>/teams/',
         views.tournament_teams, name='team_tournament_list_teams'),
    path('team-tournaments/<int:tournament_id>/',
         views.team_tournament_detail, name='team_tournament_detail'),
    path('team-tournaments/<int:tournament_id>/teams/<int:team_id>/',
         views.join_team_view, name='team_tournament_team_join'),
    path('team-tournaments/<int:tournament_id>/team-match/new/',
         views.create_team_match, name='team_tournament_create_match'),
    path('team-tournaments/<int:tournament_id>/matches/<int:pk>/edit/',
         views.TeamMatchEditView.as_view(), name='team_tournament_edit_match'),

    # index
    path('', views.index, name='index'),
]
