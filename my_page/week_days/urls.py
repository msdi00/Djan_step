from django.urls import path
from . import views

urlpatterns = [
    path("<int:week>/", views.get_week_num),
    path("hello/", views.get_week_html),
    path("<str:week>/", views.get_week, name="name-day"),
]