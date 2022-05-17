# distance/urls.py

from django.urls import path
from distance import views

urlpatterns = [
    path("", views.api_distance_between_locations_view),
]
