from django.urls import path
from . import views

urlpatterns = [
    path('accounts/profile/', views.profile, name='profile'),
    path('tournament/<int:tournament_id>/create-team/',
         views.create_team_view, name='create_team'),
    path('tournament/<int:tournament_id>/join/',
         views.join_single_tournament, name='join_single_tournament'),
    path('single-tournament/<int:tournament_id>/',
         views.single_tournament_detail, name='single_tournament_detail'),
    path('team-tournament/<int:tournament_id>/',
         views.team_tournament_detail, name='team_tournament_detail'),
    path('tournament/<int:tournament_id>/teams/',
         views.tournament_teams, name='tournament_teams'),
    path('team-participant/<int:team_id>/',
         views.join_team_view, name='join_team'),
    path('single-match/<int:tournament_id>/',
         views.create_single_match, name='create_single_match'),
    path('team-match/<int:tournament_id>/',
         views.create_team_match, name='create_team_match'),
    path('', views.index, name='index'),
]
