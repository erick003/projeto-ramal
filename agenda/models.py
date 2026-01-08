# Arquivo: agenda/models.py

from django.db import models

class Ramal(models.Model):  
    nome = models.CharField(max_length=100)
    setor = models.CharField(max_length=100)
    numero = models.CharField(max_length=20)

    def __str__(self):
        return self.nome