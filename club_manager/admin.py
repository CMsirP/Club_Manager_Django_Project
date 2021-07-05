from django.contrib import admin
from .models import Club, Group, Coach, Officer, Member, Tournament, Location, Player
# Register your models here.

admin.site.register(Club)
admin.site.register(Group)
admin.site.register(Coach)
admin.site.register(Location)
admin.site.register(Member)
admin.site.register(Player)
admin.site.register(Officer)
admin.site.register(Tournament)