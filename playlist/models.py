from django.db import models
from django.core.validators import FileExtensionValidator

class Musica(models.Model):
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=100)
    album = models.CharField(max_length=100, blank=True)
    capa = models.ImageField(upload_to='capas/', validators=[FileExtensionValidator(['png', 'jpeg', 'jpg'])])
    def __str__(self):
        return f"{self.titulo} - {self.artista}"

class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    musicas = models.ManyToManyField(Musica)  # Nome em minúsculo

    def __str__(self):
        return self.nome
