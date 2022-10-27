from django.shortcuts import render
from django.http import HttpResponse
from .models import Libro
from .forms import LibroForm
# Create your views here.

def inicio(request):
  return render(request, 'pages/inicio.html')

def nosotros(request):
  return render(request, 'pages/nosotros.html')

def libros(request):
  libros = Libro.objects.all()
  return render(request, 'pages/libros/index.html', {'libros': libros})

def crear_libro(request):
  formulario = LibroForm(request.POST or None)
  return render(request, 'pages/libros/create.html', {'formulario': formulario})

def editar_libro(request):
  return render(request, 'pages/libros/edit.html')
