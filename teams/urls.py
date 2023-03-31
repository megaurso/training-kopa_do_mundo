from django.urls import path
from .views import TeamView, TeamInfoView

urlpatterns = [
    path("teams/", TeamView.as_view()),
    path("teams/<int:team_id>/", TeamInfoView.as_view()),
]
