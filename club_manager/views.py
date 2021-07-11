from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from club_manager.models import Club, Group, Member, Player, Officer, Coach, Tournament
from .forms import ClubForm, GroupForm, MemberForm, PlayerForm, OfficerForm, CoachForm, TournamentForm


def index(request):
    return render(request, 'club_manager/index.html')


@login_required
def clubs(request):
    """Show all clubs."""
    clubs = Club.objects.filter(owner=request.user).order_by('club_name')
    context = {'clubs': clubs}
    return render(request, 'club_manager/clubs.html', context)


@login_required
def club(request, club_id):
    """Shows a single club and its details."""
    club = Club.objects.get(id=club_id)
    # Ensure that club can only be accessed by appropriate owner.
    if club.owner != request.user:
        raise Http404
    groups = club.group_set.order_by('group_name')
    members = club.member_set.order_by('name')
    officers = club.officer_set.order_by('role')
    tournaments = club.tournament_set.order_by('t_date')
    context = {
        'club': club, 'groups': groups, 'members': members,
        'officers': officers, 'tournaments': tournaments
               }
    return render(request, 'club_manager/club.html', context)


@login_required
def group(request, group_id):
    """Shows a single group and its details."""
    group = Group.objects.get(id=group_id)
    club = group.club
    if club.owner != request.user:
        raise Http404
    players = group.player_set.order_by('id')
    coaches = group.coach_set.order_by('id')
    context = {'club': club, 'group': group, 'players': players, 'coaches': coaches}
    return render(request, 'club_manager/group.html', context)


@login_required
def member(request, member_id):
    """Shows a single member and their details."""
    member = Member.objects.get(id=member_id)
    club = member.club
    if club.owner != request.user:
        raise Http404
    context = {'club': club, 'member': member}
    return render(request, 'club_manager/member.html', context)


@login_required
def tournament(request, tournament_id):
    """Shows a single member and their details."""
    tournament = Tournament.objects.get(id=tournament_id)
    club = tournament.club
    if club.owner != request.user:
        raise Http404
    players = tournament.players_list.all()
    context = {'club': club, 'players': players, 'tournament': tournament}
    return render(request, 'club_manager/tournament.html', context)


@login_required
def player(request, player_id):
    """Shows a single player and their details."""
    player = Player.objects.get(id=player_id)
    group = player.group
    club = group.club
    if club.owner != request.user:
        raise Http404
    context = {'group': group, 'player': player}
    return render(request, 'club_manager/player.html', context)


@login_required
def new_club(request):
    """Create a new club."""
    if request.method != 'POST':
        # No data submitted; create a blank form.
        form = ClubForm()
    else:
        # POST data submitted; process data.
        form = ClubForm(data=request.POST)
        if form.is_valid():
            new_club = form.save(commit=False)
            new_club.owner = request.user
            new_club.save()
            return redirect('club_manager:clubs')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'club_manager/new_club.html', context)


@login_required
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


@login_required
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


@login_required
def edit_group(request, group_id):
    """Edit an existing group."""
    group = Group.objects.get(id=group_id)
    club = group.club
    if club.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current group details.
        form = GroupForm(instance=group)
    else:
        # POST data submitted; process data.
        form = GroupForm(instance=group, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('club_manager:club', club_id=club.id)

    context = {'club': club, 'group': group, 'form': form}
    return render(request, 'club_manager/edit_group.html', context)


@login_required
def edit_member(request, member_id):
    """Edit an existing member."""
    member = Member.objects.get(id=member_id)
    club = member.club
    if club.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current member details.
        form = MemberForm(instance=member)
    else:
        # POST data submitted; process data.
        form = MemberForm(instance=member, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('club_manager:club', club_id=club.id)

    context = {'club': club, 'member': member, 'form': form}
    return render(request, 'club_manager/edit_member.html', context)


@login_required
def edit_club(request, club_id):
    """Edit an existing club."""
    club = Club.objects.get(id=club_id)
    if club.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current club details.
        form = ClubForm(instance=club)
    else:
        # POST data submitted; process data.
        form = ClubForm(instance=club, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('club_manager:club', club_id=club.id)

    context = {'club': club, 'form': form}
    return render(request, 'club_manager/edit_club.html', context)


@login_required
def edit_tournament(request, tournament_id):
    """Edit an existing tournament."""
    tournament = Tournament.objects.get(id=tournament_id)
    club = tournament.club
    if club.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # Initial request; pre-fill form with the current tournament details.
        form = TournamentForm(club_id=club.id, instance=tournament)
    else:
        # POST data submitted; process data.
        form = TournamentForm(club_id=club.id, instance=tournament, data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('club_manager:tournament', tournament_id=tournament.id)

    context = {'tournament': tournament, 'form': form}
    return render(request, 'club_manager/edit_tournament.html', context)


@login_required
def add_player(request, member_id):
    """Add a particular member as a player to a group."""
    member = Member.objects.get(id=member_id)
    club = member.club
    if club.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = PlayerForm(member.id)
    else:
        # POST data submitted; process data.
        form = PlayerForm(member.id, data=request.POST)
        if form.is_valid():
            new_player = form.save(commit=False)
            new_player.member = member
            new_player.save()
            return redirect('club_manager:club', club_id=club.id)

    context = {'club': club, 'member': member, 'form': form}
    return render(request, 'club_manager/add_player.html', context)
    

@login_required
def add_officer(request, member_id):
    """Add a particular member as an officer to their associated club."""
    member = Member.objects.get(id=member_id)
    club = member.club
    if club.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = OfficerForm()
    else:
        # POST data submitted; process data.
        form = OfficerForm(data=request.POST)
        if form.is_valid():
            new_officer = form.save(commit=False)
            new_officer.club = club
            new_officer.member = member
            new_officer.save()
            return redirect('club_manager:club', club_id=club.id)

    context = {'club': club, 'member': member, 'form': form}
    return render(request, 'club_manager/add_officer.html', context)


@login_required
def add_coach(request, group_id):
    """Add a member as a coach to a group."""
    group = Group.objects.get(id=group_id)
    club = group.club
    if club.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = CoachForm(group.id)
    else:
        # POST data submitted; process data.
        form = CoachForm(group.id, data=request.POST)
        if form.is_valid():
            new_coach = form.save(commit=False)
            new_coach.group = group
            new_coach.save()
            return redirect('club_manager:group', group_id=group.id)

    context = {'club': club, 'group': group, 'form': form}
    return render(request, 'club_manager/add_coach.html', context)


@login_required
def add_tournament(request, club_id):
    club = Club.objects.get(id=club_id)
    if club.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = TournamentForm(club.id)
    else:
        # POST data submitted; process data.
        form = TournamentForm(club.id, data=request.POST)
        if form.is_valid():
            new_tournament = form.save(commit=False)
            new_tournament.club = club
            new_tournament.save()
            form.save_m2m()
            return redirect('club_manager:club', club_id=club.id)

    context = {'club': club, 'form': form}
    return render(request, 'club_manager/add_tournament.html', context)


class PlayerDeleteView(LoginRequiredMixin, DeleteView):
    model = Player
    success_url = '/club_manager/clubs/group/{group_id}'


class OfficerDeleteView(LoginRequiredMixin, DeleteView):
    model = Officer
    success_url = '/club_manager/clubs/{club_id}/'


class CoachDeleteView(LoginRequiredMixin, DeleteView):
    model = Coach
    success_url = '/club_manager/clubs/group/{group_id}'


class TournamentDeleteView(LoginRequiredMixin, DeleteView):
    model = Tournament
    success_url = '/club_manager/clubs/{club_id}/'


class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    success_url = '/club_manager/clubs/{club_id}/'


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    success_url = '/club_manager/clubs/{club_id}/'


class ClubDeleteView(LoginRequiredMixin, DeleteView):
    model = Club
    success_url = '/club_manager/clubs/'
