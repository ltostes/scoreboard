from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('teams/<str:team_id>', views.teams, name='teams'),
    path('current_match', views.current_match, name='current_match'),
]
