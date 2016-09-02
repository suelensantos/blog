#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals # acrescentar para corrigir o erro de UnicodeDecodeError
from django.shortcuts import render
from django.http import HttpResponse
from .models import Artigo 

# Create your views here.
def index(request):
	latest = Artigo.objects.all() 
	context = {'latest': latest}
	return render(request, 'meu_blog/index.html', context)

def viewArtigo(resquest, titulo, dia, mes, ano):

	# Validação do dia ---->> Lembrar que não é referente se é número, caracter, mas verificar a partir da ideia de uma data..

	# tipo, dia só pode ser de 1 até 31
	# mes só pode de 1 até 12
	# e pro ano é preciso pensar numa exceção
	# pro título, restringe o tamanho dele.. no models.py, só vai até 100 caracteres.

	# Validação do mês 

	# Validação do ano

	text = "Título '%s', datada de %s/%s/%s." %(titulo, dia, mes, ano)
	return HttpResponse(text)

def valida_titulo(titulo):

	return 

def valida_dia(dia):

	return 

def valida_mes(mes):

	return

def valida_ano(ano):

	return

