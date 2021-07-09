from django import forms
from django.db import models
from .models import Club, Group, Member, Player, Officer, Coach, Tournament


class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = {'club_name', 'club_type'}
        labels = {'club name:', 'club type:'}


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = {'group_name'}
        labels = {'group name': ''}


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = {'name', 'birthdate', 'email', 'phone'}
        labels = {'name:', 'birthdate:', 'email:', 'primary phone number:'}


class PlayerForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = {'ability_level', 'group'}

    def __init__(self, member_id, *args, **kwargs):
        super(PlayerForm, self).__init__(*args, **kwargs)
        member = Member.objects.get(id=member_id)
        club = member.club
        self.fields['group'].queryset = Group.objects.filter(club=club.id)


class OfficerForm(forms.ModelForm):
    class Meta:
        model = Officer
        fields = {'role'}


class CoachForm(forms.ModelForm):
    class Meta:
        model = Coach
        fields = {'member'}

    def __init__(self, group_id, *args, **kwargs):
        super(CoachForm, self).__init__(*args, **kwargs)
        group = Group.objects.get(id=group_id)
        club = group.club
        self.fields['member'].queryset = Member.objects.filter(club=club.id)


class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = {'tourn_name', 'players_list', 't_date'}
        labels = {'tournament name:', 'players:', 'tournament date:'}

    def __init__(self, club_id, *args, **kwargs):
        super(TournamentForm, self).__init__(*args, **kwargs)
        club = Club.objects.get(id=club_id)
        self.fields['players_list'].queryset = Player.objects.filter(group__club_id=club.id)
