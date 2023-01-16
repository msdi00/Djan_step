from django.urls import path, register_converter
from . import views, converters

register_converter(converters.FourDigitYearConverter, 'yyyy')
register_converter(converters.MyFloatConverters, 'my_float')

urlpatterns = [
    path("", views.index, name="name-index"),
    path("type/", views.get_elements),
    path("type/<str:elem>/", views.elem_any, name="name-type"),
    path("<yyyy:zodiac>/", views.get_yyyy_converters),
    path("<int:zodiac>/", views.get_num),
    path("<my_float:zodiac>/", views.get_my_float_converters),
    path("<str:zodiac>/", views.get_any_zodiac, name="name-sign"),
]
