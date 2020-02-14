from django.contrib import admin
from .models import Player, Team, Edition, Sport, Participant, Competition, Match, Score, Point, Note

# Register your models here.
admin.site.register(Player)
admin.site.register(Team)
admin.site.register(Edition)
admin.site.register(Sport)
admin.site.register(Participant)
admin.site.register(Competition)
admin.site.register(Match)
admin.site.register(Score)
admin.site.register(Point)
admin.site.register(Note)
