from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('contatos/', views.lista_contatos, name='lista_contatos'),
    path('contatos/<int:id>/', views.detalhe_contato, name='detalhe_contato'),
]
