from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/palavras/<palavra_id>/', views.api_palavra),
]