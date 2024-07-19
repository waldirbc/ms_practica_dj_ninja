from django.urls import path
from .views import carga_csv

urlpatterns = [
    path('carga_csv/', carga_csv, name='carga_csv'),
]
