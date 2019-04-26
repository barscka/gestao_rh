from django.contrib import admin

# Register your models here.
from apps.funcionarios.models import Funcionarios

admin.site.register(Funcionarios)