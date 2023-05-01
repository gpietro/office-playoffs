from django import forms
from .models import SingleMatch, Team, Player, TeamMatch


class BaseMatchForm(forms.ModelForm):
    home_participant = None
    away_participant = None
    home_score = forms.IntegerField(min_value=0, initial=0)
    away_score = forms.IntegerField(min_value=0, initial=0)
    date = forms.DateField(widget=forms.SelectDateWidget)

    class Meta:
        abstract = True

        fields = ['home_participant', 'away_participant',
                  'date', 'home_score', 'away_score']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['home_score'].required = False
        self.fields['away_score'].required = False
        self.fields['date'].required = False

    def clean(self):
        cleaned_data = super().clean()
        home_participant = cleaned_data.get('home_participant')
        away_participant = cleaned_data.get('away_participant')

        if home_participant == away_participant:
            raise forms.ValidationError(
                "Home and away cannot be the same.")

        if self.Meta.model.objects.filter(home_participant=home_participant, away_participant=away_participant).exists():
            raise forms.ValidationError(
                "These participants have already played each other.")

        return cleaned_data


class CreateTeamMatchForm(BaseMatchForm):
    home_participant = forms.ModelChoiceField(queryset=Team.objects.all())
    away_participant = forms.ModelChoiceField(queryset=Team.objects.all())

    class Meta(BaseMatchForm.Meta):
        model = TeamMatch


class CreateSingleMatchForm(BaseMatchForm):
    home_participant = forms.ModelChoiceField(queryset=Player.objects.all())
    away_participant = forms.ModelChoiceField(queryset=Player.objects.all())

    class Meta(BaseMatchForm.Meta):
        model = SingleMatch


class UpdateSingleMatchForm(forms.ModelForm):
    class Meta:
        model = SingleMatch
        fields = ['home_score', 'away_score', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class UpdateTeamMatchForm(forms.ModelForm):
    class Meta:
        model = TeamMatch
        fields = ['home_score', 'away_score', 'date']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
