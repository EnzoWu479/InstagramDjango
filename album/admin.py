from django.contrib import admin
from .models import Foto

class ListandoFotos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'foto')
admin.site.register(Foto, ListandoFotos)