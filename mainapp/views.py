from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Player

def index(request):

    print(request.user)
    player = Player.objects.filter(id=1)[0]
    context = {"player_name": player.name, "time_2": 5}
    return render(request,'mainapp/homepage_view.html', context)

def teams(request, team_id):
    # Search for team on db and fetch data

    context = {"team_name": team_id}
    return render(request,'mainapp/team_view.html', context)

def current_match(request):

    context = {}
    return render(request,'mainapp/current_match.html', context)