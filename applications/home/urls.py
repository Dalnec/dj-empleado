from django.contrib import admin
from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('prueba/', views.PruebaView.as_view()),
    path('lista/', views.PruebaListView.as_view()),
    path('add/', views.PruebaCreateView.as_view(), name='prueba_add'),
    path('resumen-fundation/', views.ResumenFoundationView.as_view(), name='resumen_fundation'),
]