from django.urls import path
from . import views

app_name = "metrology"

urlpatterns = [
    path('', views.main, name='main'),
    path('all_measuring_instruments/', views.all_measuring_instruments, name='all_measuring_instruments'),
]