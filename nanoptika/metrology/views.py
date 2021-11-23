from django.shortcuts import render
from django.http import HttpResponse

def main(request):
    context = {
        'page_title':'Метрология',
    }
    return render(request, 'metrology/index.html', context)