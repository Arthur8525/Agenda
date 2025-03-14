from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255)
    email = models.EmailField()
    sobre = models.TextField()
    telefone = models.IntegerField()
    altura = models.DecimalField(decimal_places=2, max_digits=3)
    ativo = models.BooleanField()
    data_criacao = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nome