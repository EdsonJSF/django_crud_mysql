from django.shortcuts import render, redirect
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
  formulario = LibroForm(request.POST or None, request.FILES or None)
  if formulario.is_valid():
    formulario.save()
    return redirect('libros')
  return render(request, 'pages/libros/create.html', {'formulario': formulario})

def editar_libro(request):
  return render(request, 'pages/libros/edit.html')

def eliminar_libro(request, id):
  libro = Libro.objects.get(id=id)
  libro.delete()
  return redirect('libros')