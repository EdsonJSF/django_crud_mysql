from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def inicio(request):
  return render(request, 'pages/inicio.html')

def nosotros(request):
  return render(request, 'pages/nosotros.html')

def libros(request):
  return render(request, 'pages/libros/index.html')

def crear_libro(request):
  return render(request, 'pages/libros/create.html')