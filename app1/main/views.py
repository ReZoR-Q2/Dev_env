from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Home - Главная',
        'content': 'Главная страница магазина - HOME',
    }
    
    
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': 'О нас',
        'text_on_page': 'Текст о там почему наш магазин такой класный, и какой хороший товар.'
        
    }
    
    
    return render(request, 'main/about.html', context)