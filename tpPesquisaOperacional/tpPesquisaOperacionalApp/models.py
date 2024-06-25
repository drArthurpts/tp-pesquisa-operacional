from django.db import models

class Abrigo(models.Model):
    nome = models.CharField(max_length=200)
    capacidade = models.IntegerField()
    localizacao = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Desabrigado(models.Model):
    nome = models.CharField(max_length=200)
    localizacao_atual = models.CharField(max_length=200)
    abrigo = models.ForeignKey(Abrigo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nome