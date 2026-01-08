# setup/urls.py

from django.contrib import admin # <-- ADICIONE ESTA LINHA
from django.urls import path, include

urlpatterns = [
    # Agora 'admin' é reconhecido
    path('admin/', admin.site.urls), 
    path('', include('agenda.urls', namespace='agenda')),
]