from django.contrib import admin
from galeria.models import Fotografia


class ListandoFotografias(admin.ModelAdmin):
    list_display =("nome","id","legenda")
    list_display_links = ('nome',)
    search_fields = ("nome",)

admin.site.register(Fotografia,ListandoFotografias)
