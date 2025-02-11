from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='inicio'),
    path('obtener_solicitudes/', views.obtener_solicitudes, name='obtener_solicitudes'),
]