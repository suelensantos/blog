#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.test import TestCase
from .views import valida_titulo, valida_dia, valida_mes, valida_ano

# Create your tests here.

# EXEMPLO PARA OS MÉTODOS DE VALIDAÇÃO!
# FAZER TBM PARA OS MÉTODOS VIEWARTIGO E INDEX - ACOMPANHAR NO SITE (MAIOR O CÓDIGO)!

class ArtigoTestCase(TestCase):

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

