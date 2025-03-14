from django.shortcuts import render, get_object_or_404
from .models import Contato

def home(request):
    return render(request, 'home.html')

def lista_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'lista_contatos.html', {'contatos': contatos})

def detalhe_contato(request, id):
    contato = get_object_or_404(Contato, pk=id)
    return render(request, 'detalhe_contato.html', {'contato': contato})
