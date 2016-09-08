#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from django.test import TestCase
from django.utils import timezone
import datetime
from .views import valida_titulo, valida_dia, valida_mes, valida_ano
from .models import Artigo
from django.urls import reverse
#from django.test import Client

# Create your tests here.

# EXEMPLO PARA OS MÉTODOS DE VALIDAÇÃO!
# FAZER TBM PARA OS MÉTODOS VIEWARTIGO E INDEX - ACOMPANHAR NO SITE (MAIOR O CÓDIGO)!

class ArtigoModelTestCase(unittest.TestCase):

	def test_foi_publicado_recentemente(self):
		# foi_publicado_recentemente() deve retornar Falso para perguntas cuja publicacao é no futuro
		time  = timezone.now() + datetime.timedelta(days=30)
		pergunta_futuro = Artigo(publicacao = time)
		self.assertIs(pergunta_futuro.foi_publicado_recentemente(), False)

	def test_foi_publicado_recentemente_com_pergunta_antiga(self):
		# foi_publicado_recentemente() deve retornar Falso para perguntas cuja publicacao é mais antiga que 1 dia
		time = timezone.now() - datetime.timedelta(days=30)
		pergunta_antiga = Artigo(publicacao = time)
		self.assertIs(pergunta_antiga.foi_publicado_recentemente(), False)

	def test_foi_publicado_recentemente_com_pergunta_recente(self):
		# foi_publicado_recentemente() deve retornar True para perguntas cuja publicacao está dentro do último dia
		time = timezone.now() - datetime.timedelta(hours=1)
		pergunta_recente = Artigo(publicacao = time)
		self.assertIs(pergunta_recente.foi_publicado_recentemente(), True)

def criar_artigo(titulo, conteudo, dias):
    	# cria um artigo
    	time = timezone.now() + datetime.timedelta(days=dias)
    	return Artigo.objects.create(titulo=titulo, conteudo=conteudo, publicacao=time)

class ArtigoViewTestCase(unittest.TestCase):
 #-----
    # Teste do método index

	def test_index_sem_artigo(self):
		# Se não há artigo, uma mensagem apropriada deve ser disparada
		responder = self.client.get(reverse('meu_blog:index'))
		self.assertEqual(responder.status_code, 200)
        self.assertContains(responder, "Não há artigos disponíveis.")
        self.assertQuerysetEqual(responder.context['latest'], [])
 #-----

	# Testes para validar título

	def test_valida_titulo_valido(self):
		titulo_valido = valida_titulo('abcdefghijklmnopqrstuvwxyz')
		self.assertTrue(titulo_valido)

	def test_valida_titulo_invalido(self):
		titulo_invalido = valida_titulo('abcdefghijklmnopqrstuvwxyz|abcdefghijklmnopqrstuvwxyz|abcdefghijklmnopqrstuvwxyz|abcdefghijklmnopqrstuvwxyz')
		self.assertFalse(titulo_invalido)

	# Testes para validar dia

	def test_valida_dia_valido(self):
		dia_valido = valida_dia(10)
		self.assertTrue(dia_valido)

	def test_valida_dia_invalido(self):
		dia_invalido = valida_dia(33)
		self.assertFalse(dia_invalido)

	# Testes para validar mês

	def test_valida_mes_valido(self):
		mes_valido = valida_mes(05)
		self.assertTrue(mes_valido)

	def test_valida_mes_invalido(self):
		mes_invalido = valida_mes(15)
		self.assertFalse(mes_invalido)

	# Testes para validar ano

	def test_valida_ano_valido(self):
		ano_valido = valida_ano(2016)
		self.assertTrue(ano_valido)

	def test_valida_ano_invalido(self):
		ano_invalido = valida_ano(2060)
		self.assertFalse(ano_invalido)

