from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from apps.departamentos.models import Departamento
from apps.empresas.models import Empresas

class Funcionarios(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    departamentos = models.ManyToManyField(Departamento)
    empresa = models.ForeignKey(Empresas, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome