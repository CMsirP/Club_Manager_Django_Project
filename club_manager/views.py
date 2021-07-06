from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from club_manager.models import Club, Group


def index(request):
    return render(request, 'club_manager/index.html')


def clubs(request):
    """Show all clubs."""
    clubs = Club.objects.order_by('club_name')
    context = {'clubs': clubs}
    return render(request, 'club_manager/clubs.html', context)


def club(request, club_id):
    """Shows a single club and its details."""
    club = Club.objects.get(id=club_id)
    groups = club.group_set.order_by('group_name')
    context = {'club': club, 'groups': groups}
    return render(request, 'club_manager/club.html', context)


def group(request, group_id):
    """Shows a single group and its details."""
    group = Group.objects.get(id=group_id)
    players = group.player_set.order_by('player_id')
    coach = group.coach_set.order_by('coach_id')
    context = {'group': group, 'players': players}
    return render(request, 'club_manager/group.html', context)
