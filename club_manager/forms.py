from django import forms
from django.db import models
from .models import Club, Group, Member, Player


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


