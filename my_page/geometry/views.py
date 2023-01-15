from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
import math
from django.urls import reverse

figure_area = {
    "rectangle": lambda x, y: x * y,
    "square": lambda x: x * x,
    "circle": lambda x: math.pi * x ** 2,
}

names_figure_area = {
    "get_square_area": "square",
    "get_circle_area": "circle",
    "get_rectangle_area": "rectangle",
}

description = {
    "square": 'f"Площадь квадрата размером {x} x {x} равна {figure_area[figur](x)}"',
    "circle": 'f"Площадь треугольника размером π x {x}^2 равна {figure_area[figur](x)}"',
    "rectangle": 'f"Площадь прямоугольника размером {x} x {y} равна {figure_area[figur](x, y)}"',
}


def figur_area(request, figur, x=0, y=0):
    return HttpResponse(eval(description[figur]))


def get_rectangle_area(request, x=0, y=0):
    redirect_url = reverse("geom-name", args=("square", x, y))
    return HttpResponseRedirect(redirect_url)
