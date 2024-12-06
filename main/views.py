from django.shortcuts import render


def index(request):
    context = {
        'title': 'Главная страница',
        'name': 'Грегорий'
    }

    return render(request, 'main/index.html', context)