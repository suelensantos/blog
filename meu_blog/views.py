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

def viewArtigo(request, titulo, dia, mes, ano):

	params = {'erro': False, 'msg': 'Sucesso!', 'titulo': titulo, 'dia': dia, 'mes': mes, 'ano': ano}
	# Validação do dia 

	#if not valida_dia(dia):

		#text = "O dia %s não é um dia válido." % dia
		#return HttpResponse(text)
# -------

	# Validação do Título

 	#if not valida_titulo(titulo):
 		#return render(request, 'meu_blog/artigo.html', {'titulo': titulo, 'dia': dia, 'mes': mes, 'ano': ano})

	# Validação do dia 

	if not valida_dia(dia):
		params['erro'] = True
		params['msg'] = "O dia %s não é uma dia válido." % dia

	# Validação do mês 

	#if not valida_mes(mes):
		#return render(request, 'meu_blog/artigo.html', {'titulo': titulo, 'dia': dia, 'mes': mes, 'ano': ano})

	# Validação do ano

	#if not valida_ano(ano):
		#return render(request, 'meu_blog/artigo.html', {'titulo': titulo, 'dia': dia, 'mes': mes, 'ano': ano})

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

	if 0 < mes <= 12:
		return True
	return False

def valida_ano(ano):

	if  1900 <= ano <= 2050:
		return True
	return False

