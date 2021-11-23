from django.shortcuts import render

def home(request):
    context = {
        'page_title':'Главная',
    }
    return render(request, 'nanoptika/home.html', context)