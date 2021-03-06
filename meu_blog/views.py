#!/usr/bin/env python
# -*- coding: utf-8 -*-

# acrescentar para corrigir o erro de UnicodeDecodeError
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Artigo
from .forms import FormContato

# Create your views here.


def index(request):
    latest = Artigo.objects.all()
    context = {'latest': latest}
    return render(request, 'meu_blog/index.html', context)


def indexArtigo(request, artigo_id):
    artigo = Artigo.objects.get(id=artigo_id)
    context = {'artigo': artigo}
    return render(request, 'meu_blog/index_artigo.html', context)


def viewArtigo(request, titulo, dia, mes, ano):

    params = {'msg': [], 'titulo': titulo, 'dia': dia, 'mes': mes, 'ano': ano}

    # Validação do título

    if not valida_titulo(titulo):
        params['msg'].append("ERRO-01! O título %s não é válido." % titulo)

    # Validação do dia

    if not valida_dia(dia):
        params['msg'].append("ERRO-02! O dia %s não é válido." % dia)

    # Validação do mês

    if not valida_mes(mes):
        params['msg'].append("ERRO-03! O mês %s não é válido." % mes)

    # Validação do ano

    if not valida_ano(ano):
        params['msg'].append("ERRO-04! O ano %s não é válido." % ano)

    return render(request, 'meu_blog/artigo.html', params)


def valida_titulo(titulo):

    if len(titulo) <= 100:
        return True
    return False


def valida_dia(dia):

    if 0 < int(dia) <= 31:
        return True
    return False


def valida_mes(mes):

    if 0 < int(mes) <= 12:
        return True
    return False


def valida_ano(ano):

    if 1900 <= int(ano) <= 2050:
        return True
    return False


def contato(request):
    mostrar = 'Envie um contato!'
    if request.method == 'POST':
        form = FormContato(request.POST)

        if form.is_valid():
            mostrar = form.enviar()
            form = FormContato()
    else:
        form = FormContato()

    context = {'mostrar': mostrar, 'form': form}
    return render(request, 'meu_blog/contato.html', context)


def sobreMim(request):
    return render(request, 'meu_blog/sobre-mim.html')
