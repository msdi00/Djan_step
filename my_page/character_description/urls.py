from django.urls import path
from . import views

urlpatterns = [
    path("keanu/", views.get_inf_character),
    path("cites", views.get_guinness_world_records),
]