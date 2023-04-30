from django.contrib import admin

from .models import SingleMatch, SingleTournament, TeamMatch, TeamTournament, Player, Team

admin.site.site_header = 'Sparrow Tournament Admin'
admin.site.site_title = 'Sparrow Tournament Admin'
admin.site.index_title = 'Sparrow Tournament Admin'

admin.site.register(SingleTournament)
admin.site.register(TeamTournament)
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(SingleMatch)
admin.site.register(TeamMatch)
