from django.urls import path

from . import views

app_name = 'club_manager'
urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    # Club viewer
    path('clubs/', views.clubs, name='clubs')
]
