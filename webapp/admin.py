from django.contrib import admin

from .models import SingleTournament, TeamTournament, SingleParticipant, TeamParticipant

admin.site.site_header = 'Sparrow Tournament Admin'
admin.site.site_title = 'Sparrow Tournament Admin'
admin.site.index_title = 'Sparrow Tournament Admin'

admin.site.register(SingleTournament)
admin.site.register(TeamTournament)
admin.site.register(SingleParticipant)
admin.site.register(TeamParticipant)