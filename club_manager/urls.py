from django.urls import path

from . import views

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
    # Form page to add new club
    path('new_club/', views.new_club, name='new_club'),
    # Form page for adding a new group to a club
    path('new_group/<int:club_id>/', views.new_group, name='new_group'),
    # Form page for adding a new member to a club
    path('new_member/<int:club_id>/', views.new_member, name='new_member')
]
