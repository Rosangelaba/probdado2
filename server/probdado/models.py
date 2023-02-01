from django.db import models


class Combinacao(models.Model):
    dado1 = models.IntegerField()
    dado2 = models.IntegerField()
#    CorDado1 = models.CharField(max_length=10)
#    CorDado2 = models.CharField(max_length=10)

class Dica(models.Model):
    text = models.CharField(max_length=256)
    combinacoes = models.ManyToManyField(Combinacao)

