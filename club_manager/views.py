from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from club_manager.models import *


def index(request):
    return render(request, 'club_manager/index.html')


def clubs(request):
    all_clubs = Club.objects.order_by('club_name')

