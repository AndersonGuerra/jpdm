from django.db import models
#from PIL import Image


class Alimentacao(models.Model):
    tipo = models.CharField(max_length=100)
    def __str__(self):
        return self.tipo


class Ordem(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.TextField()
    def __str__(self):
        return self.nome


class Subordem(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.TextField()
    def __str__(self):
        return self.nome


class Genero(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.TextField()
    def __str__(self):
        return self.nome


class Especie(models.Model):
    nome = models.CharField(max_length=250)
    descricao = models.TextField()
    f_genero = models.ForeignKey(Genero)
    def __str__(self):
        return self.nome

class Dinossauro(models.Model):
    nome_br = models.CharField(max_length=250)
    custo_individual = models.FloatField()
    quantidade = models.IntegerField()
    imagem = models.ImageField(upload_to='imagens/dinos', null=True, blank=True)
    f_alimentacao = models.ForeignKey(Alimentacao)
    f_especie = models.ForeignKey(Especie)
    f_genero = models.ForeignKey(Genero)
    f_subordem = models.ForeignKey(Subordem)
    f_ordem = models.ForeignKey(Ordem)
