from django.shortcuts import render
from .models import MeasuringInstrument, CalibrationResult

def main(request):
    context = {
        'page_title':'Метрология',
    }
    return render(request, 'metrology/index.html', context)

def all_measuring_instruments(request):
    instruments = MeasuringInstrument.objects.all()
    return render(request, 'metrology/all_measuring_instruments.html', {'instruments':instruments})