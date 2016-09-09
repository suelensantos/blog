#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ****** import pdb; pdb.set_trace() -> comandos: pp dir(variável); c (sair); n (next); l (posição que parou); response.content (apresenta o conteúdo); ... ******

from django.test import TestCase

from django.utils import timezone
import datetime

from .views import valida_titulo, valida_dia, valida_mes, valida_ano, viewArtigo
from .models import Artigo
from django.core.urlresolvers import reverse
from django.test.client import Client

# Create your tests here.

def criar_artigo(titulo, conteudo):
    	# cria um artigo
    	return Artigo.objects.create(titulo=titulo, conteudo=conteudo, publicacao=timezone.now())

class ArtigoModelTestCase(TestCase):

	'''def test_artigo_criacao(self):
		artigo = criar_artigo(titulo='Somente um teste', conteudo='Sim, isso é apenas um teste.', dias=9)
		self.assertTrue(isinstance(artigo, Artigo))
		self.assertEqual(artigo.__unicode__(), artigo.titulo)'''

	# --- TESTES PARA FUNÇÃO FOI_PUBLICADO_RECENTEMENTE()

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


class ArtigoViewTestCase(TestCase):

	def setUp(self):
		self.client = Client()

    # --- TESTES PARA FUNÇÃO INDEX()

	def test_index_view_sem_artigo(self):
		# Se não há artigo, uma mensagem apropriada deve ser exibida
		response = self.client.get(reverse('index'))
		self.assertEqual(response.status_code, 200)
		self.assertIn('Sem artigos.', response.content)
		self.assertQuerysetEqual(response.context['latest'], [])

	def test_index_view_com_artigo(self):
		# Se há artigo, uma mensagem apropriada deve ser exibida
		criar_artigo(titulo='Somente um teste', conteudo='Sim, isso eh apenas um teste.')
		response = self.client.get(reverse('index'))
		self.assertQuerysetEqual(response.context['latest'], ['<Artigo: Somente um teste>'])

    # --- TESTES PARA FUNÇÃO VIEWARTIGO()
    # *** Dada a entrada da função, a saída corresponde igual? ***
    # com o artigo criado, ver se os parâmetros da entrada batem com a da saída

    #def test_viewArtigo_mensagem_de_erro(self):
    #	itens = 

 	# --- TESTES PARA FUNÇÕES VALIDA...()

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

