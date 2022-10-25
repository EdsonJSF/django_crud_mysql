from xml.dom.minidom import Document
from django.urls import path
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
  path('', views.inicio, name='inicio'),
  path('nosotros', views.nosotros, name='nosotros'),
  path('libros', views.libros, name='libros'),
  path('libros/crear', views.crear_libro, name='crear_libro'),
  path('libros/editar', views.editar_libro, name='editar_libro'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
