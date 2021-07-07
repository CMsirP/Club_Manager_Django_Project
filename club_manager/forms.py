from django import forms
from .models import Club, Group, Member


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
