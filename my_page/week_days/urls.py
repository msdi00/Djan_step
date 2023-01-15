from django.urls import path
from . import views

urlpatterns = [
    path("<int:week>/", views.get_week_num),
    path("<str:week>/", views.get_week, name="name-day"),
    path("hello/", views.get_week_html),
]