from django.urls import path
from analytics import views

urlpatterns = [
    path("", views.api_ordered_locations_view),
]
