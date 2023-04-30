from django import forms
from .models import SingleMatch, Team, Player, TeamMatch


class CreateTeamMatchForm(forms.ModelForm):
    home_participant = forms.ModelChoiceField(queryset=Team.objects.all())
    away_participant = forms.ModelChoiceField(queryset=Team.objects.all())

    class Meta:
        model = TeamMatch
        fields = ['home_participant', 'away_participant']

    def clean(self):
        cleaned_data = super().clean()
        home_participant = cleaned_data.get('home_participant')
        away_participant = cleaned_data.get('away_participant')

        if home_participant == away_participant:
            raise forms.ValidationError(
                "Home and away team cannot be the same.")

        if TeamMatch.objects.filter(home_participant=home_participant, away_participant=away_participant).exists():
            raise forms.ValidationError(
                "These teams/players have already played each other.")

        return cleaned_data


class CreateSingleMatchForm(forms.ModelForm):
    home_participant = forms.ModelChoiceField(queryset=Player.objects.all())
    away_participant = forms.ModelChoiceField(queryset=Player.objects.all())

    class Meta:
        model = SingleMatch
        fields = ['home_participant', 'away_participant']

    def clean(self):
        cleaned_data = super().clean()
        home_participant = cleaned_data.get('home_participant')
        away_participant = cleaned_data.get('away_participant')

        if home_participant == away_participant:
            raise forms.ValidationError(
                "Home and away player cannot be the same.")

        if SingleMatch.objects.filter(home_participant=home_participant, away_participant=away_participant).exists():
            raise forms.ValidationError(
                "These teams/players have already played each other.")

        return cleaned_data
