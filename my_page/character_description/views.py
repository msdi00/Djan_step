from django.shortcuts import render

def get_inf_character(request):
    data = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'The matrix'
    }
    return render(request, "character_description/characters.html", context=data)

