from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
from django.shortcuts import render
from dataclasses import dataclass


@dataclass
class DescriptionCars:
    # test module dataclasses
    model: str
    brand: str


zodiac_dct = {
    'aries': 'Овен	21 марта – 20 апреля',
    'taurus': 'Телец	21 апреля – 21 мая',
    'gemini': 'Близнецы	22 мая – 21 июня',
    'cancer': 'Рак	22 июня – 22 июля',
    'leo': 'Лев	23 июля – 23 августа',
    'virgo': 'Дева	24 августа – 22 сентября',
    'libra': 'Весы	23 сентября – 23 октября',
    'scorpio': 'Скорпион	24 октября – 22 ноября',
    'sagittarius': 'Стрелец	23 ноября – 21 декабря',
    'capricorn': 'Козерог	22 декабря – 20 января',
    'aquarius': 'Водолей	21 января – 18 февраля',
    'pisces': 'Рыбы	19 февраля – 20 марта',
}

elements = {
    "fire": ["aries", "leo", "sagittarius"],
    "water": ["cancer", "scorpio", "pisces"],
    "air": ["gemini", "libra", "aquarius"],
    "ground": ["taurus", "virgo", "capricorn"]
}


def get_yyyy_converters(request, zodiac):
    return HttpResponse(f"Вы передали число из 4 цифр {zodiac}")


def get_my_float_converters(request, zodiac):
    return HttpResponse(f"Вы передали число из вещественного числа - {zodiac}")


def get_any_zodiac(request, zodiac):
    # contains tests set command for rendering HTML
    description = zodiac_dct.get(zodiac)
    data = {
        'descr_zodiac': description,
        'name_zodiac': zodiac
        # 'nums_tuple': (1, 2, 3),
        # 'name_class': DescriptionCars('volvo', 'S90'),
    }
    return render(request, "horoscope/info_zodiac.html", context=data)


def get_num(request, zodiac):
    if zodiac > len(zodiac_dct):
        return HttpResponse('Неправильный порядковый номер зодиака')
    zodiac_lst = list(zodiac_dct)
    name_zodiac = zodiac_lst[zodiac - 1]
    response_url = reverse("name-sign", args=(name_zodiac,))
    print(response_url)
    return HttpResponseRedirect(response_url)


# def index(request):
#     # generating variable str for HTML
#     zodiac_lst = list(zodiac_dct)
#     li_elements = "".join(
#         f"<li><a href='{reverse('name-sign', args=(zodiac,))}'>{zodiac.title()}</a></li>" for zodiac in zodiac_lst)
#     response = f"""
#     <ol>
#         {li_elements}
#     </ol>
#     """
#     return HttpResponse(response)

def index(request):
    zodiacs_lst = list(zodiac_dct)
    context = {
        'zodiacs': zodiacs_lst,
    }
    return render(request, 'horoscope/index.html', context=context)

def get_elements(request):
    elements_lst = list(elements)
    li_elem = "".join(
        f"<li><a href='{reverse('name-type', args=(elem,))}'>{elem.title()}</a></li>" for elem in elements_lst)
    response = f"""
        <ol>
            {li_elem}
        </ol>
        """
    return HttpResponse(response)

# def get_elements(request):
#     elements_lst = list(elements)
#     context = {
#         'elements': elements_lst,
#     }
#     return render(request, 'horoscope/get_elements.html', context=context)


def elem_any(request, elem):
    li_elem = "".join(
        f"<li><a href='{reverse('name-sign', args=(elem,))}'>{elem.title()}</a></li>" for elem in elements[elem])
    response = f"""
            <ol>
                {li_elem}
            </ol>
            """
    return HttpResponse(response)
