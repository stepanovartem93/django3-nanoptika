from django.urls import path
from . import views

app_name = "metrology"

urlpatterns = [
    path('', views.main, name='main'),
]