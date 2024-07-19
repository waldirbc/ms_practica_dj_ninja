from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI
from api_usuarios.views import api as usuarios_api

api = NinjaAPI()
api.add_router("/api/", usuarios_api)

urlpatterns = [
    path('', api.urls),
]
