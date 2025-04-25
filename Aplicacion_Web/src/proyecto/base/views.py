from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def lista_pendientes(pedido):
    return HttpResponse("Lista de pendientes")
