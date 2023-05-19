from django.contrib import admin

from garagem.models import Marca, Categoria, Acessorio, Cor, Modelo, Veiculo

admin.site.register(Marca)
admin.site.register(Categoria)
admin.site.register(Acessorio)
admin.site.register(Cor)
admin.site.register(Modelo)
admin.site.register(Veiculo)

# Register your models here.
