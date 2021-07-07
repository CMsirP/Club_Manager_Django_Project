from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from club_manager.models import Club, Group, Member
from .forms import ClubForm, GroupForm, MemberForm


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
    members = club.member_set.order_by('name')
    context = {'club': club, 'groups': groups, 'members': members}
    return render(request, 'club_manager/club.html', context)


def group(request, group_id):
    """Shows a single group and its details."""
    group = Group.objects.get(id=group_id)
    club = group.club
    players = group.player_set.order_by('player_id')
    coaches = group.coach_set.order_by('coach_id')
    context = {'club': club, 'group': group, 'players': players, 'coaches': coaches}
    return render(request, 'club_manager/group.html', context)


def member(request, member_id):
    """Shows a single member and their details."""
    member = Member.objects.get(id=member_id)
    club = member.club
    context = {'club': club, 'member': member}
    return render(request, 'club_manager/member.html', context)


def new_club(request):
    """Create a new club."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ClubForm()
    else:
        # POST data submitted; process data.
        form = ClubForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('club_manager:clubs')
    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'club_manager/new_club.html', context)


def new_group(request, club_id):
    """Create a new group for a particular club."""
    club = Club.objects.get(id=club_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = GroupForm()
    else:
        # POST data submitted; process data.
        form = GroupForm(data=request.POST)
        if form.is_valid():
            new_group = form.save(commit=False)
            new_group.club = club
            new_group.save()
            # Redirect to the group's associated club.
            return redirect('club_manager:club', club_id=club_id)
    # Display a blank or invalid form.
    context = {'club': club, 'form': form}
    return render(request, 'club_manager/new_group.html', context)


def new_member(request, club_id):
    """Create a new member associated with a particular club."""
    club = Club.objects.get(id=club_id)

    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = MemberForm()
    else:
        # POST data submitted; process data.
        form = MemberForm(data=request.POST)
        if form.is_valid():
            new_member = form.save(commit=False)
            new_member.club = club
            new_member.save()
            # Redirect to the group's associated club.
            return redirect('club_manager:club', club_id=club_id)
    # Display a blank or invalid form.
    context = {'club': club, 'form': form}
    return render(request, 'club_manager/new_member.html', context)
