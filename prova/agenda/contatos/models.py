from django.db import models

class Contato(models.Model):
    nome =  models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.nome