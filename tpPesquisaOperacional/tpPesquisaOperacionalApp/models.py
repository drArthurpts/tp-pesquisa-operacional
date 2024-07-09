from django.db import models

class Abrigo(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    capacidade = models.IntegerField()
    localizacao = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return self.nome

class Desabrigado(models.Model):
    nome = models.CharField(max_length=200, null=False, blank=False)
    idade = models.IntegerField(default=0, null=False, blank=False)
    sexo = models.CharField(max_length=1, null=False, blank=False)
    def __str__(self):
        return self.nome