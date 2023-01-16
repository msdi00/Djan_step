from django.shortcuts import render


def get_inf_character(request):
    data = {
        'year_born': 1964,
        'city_born': 'Бейрут',
        'movie_name': 'The matrix'
    }
    return render(request, "character_description/characters.html", context=data)


def get_guinness_world_records(request):
    context = {
        'power_man': 'Navil',
        'bar_name': 'Big Bob`s sdf s sdf',
        'count_needle': 1970,
    }
    return render(request, 'character_description/guinnessworldrecords.html', context=context)
