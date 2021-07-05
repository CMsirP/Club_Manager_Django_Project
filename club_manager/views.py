from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from club_manager.models import *


def index(request):
    return HttpResponse("Stub for manager index")


# def club_page(request, c_name):
#     club = get_object_or_404(Club, club_name=c_name)
