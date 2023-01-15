from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

week_inf = {
    'monday': 'Понедельник',
    'tuesday': 'Вторник',
    'wendsday': 'Среда',
    'thursday': 'Четверг',
    'friday': 'Пятница',
    'saturday': 'Суббота',
    'sunday': 'Воскресенье'
}


# Create your views here.
def get_week(request, week: str):
    if week_inf.get(week, None):
        return HttpResponse(f'Сегодня {week_inf[week]}')
    else:
        return HttpResponseNotFound(f' День {week} не найден')


def get_week_num(request, week: int):
    if week > len(week_inf):
        return HttpResponseNotFound(f'Неверный номер дня: {week}')
    week_lst = list(week_inf)
    name_day = week_lst[week - 1]
    response_url = reverse("name-day", args=(name_day, ))
    return HttpResponseRedirect(response_url)


def get_week_html(request):
    response = render_to_string('week_days/greeting.html')
    return HttpResponse(response)
