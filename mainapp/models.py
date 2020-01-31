from django.db import models

# Create your models here.

class Player(models.Model):
    name = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)
    players = models.ForeignKey(Player, on_delete=models.CASCADE)
    img_url = models.URLField()
