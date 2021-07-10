from django.urls import path

from . import views
from .views import (
                    PlayerDeleteView, OfficerDeleteView, CoachDeleteView,
                    TournamentDeleteView, MemberDeleteView, GroupDeleteView,
                    ClubDeleteView)

app_name = 'club_manager'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Club viewer
    path('clubs/', views.clubs, name='clubs'),
    # Detail page for a single club
    path('clubs/<int:club_id>/', views.club, name="club"),
    # Detail page for a single group
    path('clubs/group/<int:group_id>', views.group, name="group"),
    # Detail page for a single member
    path('clubs/member/<int:member_id>', views.member, name='member'),
    # Detail page for a single player
    path('clubs/player/<int:player_id>', views.player, name='player'),
    # Form page to add new club
    path('new_club/', views.new_club, name='new_club'),
    # Form page for adding a new group to a club
    path('new_group/<int:club_id>/', views.new_group, name='new_group'),
    # Form page for adding a new member to a club
    path('new_member/<int:club_id>/', views.new_member, name='new_member'),
    # Page for editing a particular group
    path('edit_group/<int:group_id>/', views.edit_group, name='edit_group'),
    # Page for editing a particular member
    path('edit_member/<int:member_id>/', views.edit_member, name='edit_member'),
    # Page for editing a particular club
    path('edit_club/<int:club_id>/', views.edit_club, name='edit_club'),
    # Page for adding a member as a player to a group
    path('add_player/<int:member_id>/', views.add_player, name='add_player'),
    # Page for adding a member as an officer to a club
    path('add_officer/<int:member_id>/', views.add_officer, name='add_officer'),
    # Page for adding a member as a coach to a group
    path('add_coach/<int:group_id>/', views.add_coach, name='add_coach'),
    # Page for adding a tournament to the club
    path('add_tournament/<int:club_id>/', views.add_tournament, name='add_tournament'),
    # Detail page for a single tournament
    path('tournament/<int:tournament_id>/', views.tournament, name='tournament'),
    # Page for editing a particular tournament
    path('edit_tournament/<int:tournament_id>/', views.edit_tournament, name='edit_tournament'),
    # Page for deleting a player from a group
    path('delete_player/<pk>', PlayerDeleteView.as_view(), name='delete_player'),
    # Page for deleting an officer from a club
    path('delete_officer/<pk>', OfficerDeleteView.as_view(), name='delete_officer'),
    # Page for deleting a coach from a club
    path('delete_coach/<pk>', CoachDeleteView.as_view(), name='delete_coach'),
    # Page for deleting a tournament from a club
    path('delete_tournament/<pk>', TournamentDeleteView.as_view(), name='delete_tournament'),
    # Page for deleting a member from a club
    path('delete_member/<pk>', MemberDeleteView.as_view(), name='delete_member'),
    # Page for deleting a group from a club
    path('delete_group/<pk>', GroupDeleteView.as_view(), name='delete_group'),
    # Page for deleting a club
    path('delete_club/<pk>', ClubDeleteView.as_view(), name='delete_club')
]
