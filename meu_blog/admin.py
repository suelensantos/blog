# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Artigo, Contato

# Register your models here.
# admin.site.register(Artigo)


class ArtigoAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informações do Título', {'fields': ['titulo']}),
        ('Informações do Conteúdo', {'fields': ['conteudo']}),
        ('Informações da Data', {'fields': ['publicacao']}),
    ]

    list_display = ('titulo', 'publicacao', 'foi_publicado_recentemente')
    list_filter = ['publicacao']
    search_fields = ['titulo']


class ContatoAdmin(admin.ModelAdmin):

    list_display = ('nome', 'email')
    list_filter = ['nome']
    search_fields = ['nome']


admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Contato, ContatoAdmin)
