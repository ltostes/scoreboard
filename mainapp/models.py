from django.db import models

# Create your models here.

class Player(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    # TO DO: Image field LOGO 
    # TO DO: Team COLORS
    description = models.TextField(blank=True)
    anthem      = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Edition(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    start_date  = models.DateField()
    end_date    = models.DateField()
    location    = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Sport(models.Model):
    SCORINGMETHOD_CHOICES = [
    ('P', 'Points'),
    ('W', 'Win or Lose')
]
    sport_category = models.CharField(max_length=100,blank=True, null=True)
    # TO DO - Think of breakdown of types and how they are structured: Points or just win, single match for 4 teams or play-offs
    scoring_method = models.CharField(max_length=1, choices=SCORINGMETHOD_CHOICES,default='W')
    playoffs = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.sport_category


class Participant(models.Model):
    player      = models.ForeignKey(Player, on_delete=models.CASCADE)
    team        = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True)
    edition     = models.ForeignKey(Edition, on_delete=models.CASCADE)
    
    profile           = models.TextField(blank=True, null=True)
    subscription_at   = models.DateTimeField(auto_now_add=True)
    update_at         = models.DateTimeField(auto_now=True)
    confirmation_at   = models.DateTimeField(blank=True, null=True)
    confirmed         = models.BooleanField(default = False)

    def __str__(self):
        return str(self.player) + ", " + str(self.team)


class Competition(models.Model):
    winner        = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True, related_name='winner_%(class)s')
    second        = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True, related_name='second_placed_%(class)s')
    third         = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True, related_name='third_placed_%(class)s')
    fourth        = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True, related_name='fourth_placed_%(class)s')

    edition       = models.ForeignKey(Edition, on_delete=models.CASCADE)
    sport         = models.ForeignKey(Sport, on_delete=models.SET_NULL, blank=True, null=True)

    started       = models.BooleanField(default = False)
    finished      = models.BooleanField(default = False)
    start_time    = models.DateTimeField(blank=True, null=True)
    finish_time   = models.DateTimeField(blank=True, null=True)

    comments = models.TextField(blank=True, null=True)

    first_second_draw = models.BooleanField(default = False)
    second_third_draw = models.BooleanField(default = False)
    third_fourth_draw = models.BooleanField(default = False)

    def __str__(self):
        return str(self.sport) + ", " + str(self.edition)


class Match(models.Model):
    PLAYOFFROUND_CHOICES = [
    ('SF1', 'Semi-final 1'),
    ('SF2', 'Semi-final 2'),
    ('F', 'Final'),
    ('3', '3rd Place Dispute')
]
    competition   = models.ForeignKey(Competition, on_delete=models.CASCADE)
    description   = models.TextField(blank=True, null=True)

    started       = models.BooleanField(default = False)
    finished      = models.BooleanField(default = False)
    start_time    = models.DateTimeField(blank=True, null=True)
    finish_time   = models.DateTimeField(blank=True, null=True)

    playoff_round = models.CharField(max_length=3, choices=PLAYOFFROUND_CHOICES,blank=True, null=True)

    def __str__(self):
        if self.competition.sport.playoffs:
            return str(self.playoff_round) + " of " + str(self.competition)
        return str(self.competition)
    

class Score(models.Model):
    team        = models.ForeignKey(Team, on_delete=models.CASCADE)
    match       = models.ForeignKey(Match, on_delete=models.CASCADE)

    scored      = models.IntegerField(default = 0)

    def __str__(self):
        return str(self.team) + " scored " + str(self.scored) + " in " + str(self.match)
    

class Point(models.Model):
    participant = models.ForeignKey(Participant, on_delete=models.SET_NULL, blank=True, null=True)
    score       = models.ForeignKey(Score, on_delete=models.CASCADE)

    value       = models.IntegerField(default = 1)

    created_at  = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)

class Note(models.Model):
    taken_by    = models.ForeignKey(Participant, on_delete=models.SET_NULL, blank=True, null=True, related_name='takenby_%(class)s')
    about       = models.ForeignKey(Participant, on_delete=models.CASCADE, blank=True, null=True, related_name='about_%(class)s')

    comments = models.TextField(blank=True, null=True)

    created_at  = models.DateTimeField(auto_now_add=True)
    update_at   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.taken_by) + ", sobre " + str(self.about)
