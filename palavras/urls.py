from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/palavras/token/', views.api_get_token),
    path('api/cadastro/', views.api_cadastro),
    path('api/palavras/<palavra_id>/', views.api_palavra),
]