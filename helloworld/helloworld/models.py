from django.db import models

# Create your models here.
# CRIANDO A CLASSE FUNCIONARIO (herdando a classe Model)


class Funcionario(models.Model):
    # Entidade nome e seus respectivos campos
    nome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    # Entidade sobrenome e seus respectivos campos
    sobrenome = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    # Entidade cpf e seus respectivos campos
    cpf = models.CharField(
        max_length=14,
        null=False,
        blank=False
    )
    # Entidade tempo de serviço e seus respectivos campos
    tempo_de_servico = models.IntegerField(
        default=0,
        null=False,
        blank=False
    )
    # Entidade remuneracao e seus respectivos campos
    remuneracao = models.DecimalField(
       max_digits=8,
       decimal_places=2,
       null=False,
       blank=False
    )

    objetos = models.Manager()


#REFERENCIAS
# 1- cada campo tem um tipo
# 2- Charfield é String
# 3- PositiveIntegerField é inteiro positivo
# 4- DecimalField é um decimal com precisão fixa (geralmente para valores monetários)
# 5- o campo objetos = models.Manager() é utilizado para fazer operações de busca
# #