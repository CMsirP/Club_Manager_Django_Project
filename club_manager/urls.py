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
    # Form page to add new club
    path('new_club/', views.new_club, name='new_club'),
]
