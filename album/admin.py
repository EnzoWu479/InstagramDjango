from django.contrib import admin
from .models import Foto

class ListandoFotos(admin.ModelAdmin):
    list_display = ('id','photo','description','profile','private')
admin.site.register(Foto, ListandoFotos)