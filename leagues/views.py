from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	atlantic_conference_id = League.objects.filter(name="Atlantic Soccer Conference").first().id
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseball_leagues": League.objects.filter(sport="Baseball"),
		"womens_leagues": League.objects.filter(name__icontains="women"),
		"not_football_leagues": League.objects.exclude(sport="Football"),
		"t_teams": Team.objects.filter(team_name__istartswith="T"),
		"reverse_alpha_teams": Team.objects.all().order_by("-team_name"),
		"atlantic_teams": Team.objects.filter(league_id=atlantic_conference_id),
		"sophia_teams": Team.objects.filter(curr_players__first_name="Sophia")
	}
	print(Team.objects.filter(team_name__istartswith="T").query)
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)



	return redirect("index")