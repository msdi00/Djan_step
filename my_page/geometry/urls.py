from django.urls import path
from . import views

urlpatterns = [
    path("get_rectangle_area/<int:x>/<int:y>/", views.get_rectangle_area),
    path("<str:figur>/<int:x>/<int:y>/", views.figur_area, name="geom-name"),
    path("<str:figur>/<int:x>/", views.figur_area, name="geom-name"),
]
