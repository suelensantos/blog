#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ****** import pdb; pdb.set_trace()
# -> comandos: pp dir(variável); c (sair); n (next);
# l (posição que parou); response.content (apresenta o conteúdo); ... ******

from django.test import TestCase
from django.utils import timezone
import datetime
from .views import valida_titulo, valida_dia, valida_mes, valida_ano
from .models import Artigo
from django.core.urlresolvers import reverse
from django.test.client import Client

# Create your tests here.


def criar_artigo(titulo, conteudo):
    # cria um artigo
    return Artigo.objects.create(titulo=titulo,
                                 conteudo=conteudo,
                                 publicacao=timezone.now())


class ArtigoModelTestCase(TestCase):

    # --- TESTES PARA FUNÇÃO FOI_PUBLICADO_RECENTEMENTE()

    def test_foi_publicado_recentemente(self):
        # foi_publicado_recentemente() deve retornar Falso
        # para perguntas cuja publicacao é no futuro
        time = timezone.now() + datetime.timedelta(days=30)
        pergunta_futuro = Artigo(publicacao=time)
        self.assertIs(pergunta_futuro.foi_publicado_recentemente(), False)

    def test_foi_publicado_recentemente_com_pergunta_antiga(self):
        # foi_publicado_recentemente() deve retornar Falso
        # para perguntas cuja publicacao é mais antiga que 1 dia
        time = timezone.now() - datetime.timedelta(days=30)
        pergunta_antiga = Artigo(publicacao=time)
        self.assertIs(pergunta_antiga.foi_publicado_recentemente(), False)

    def test_foi_publicado_recentemente_com_pergunta_recente(self):
        # foi_publicado_recentemente() deve retornar True
        # para perguntas cuja publicacao está dentro do último dia
        time = timezone.now() - datetime.timedelta(hours=1)
        pergunta_recente = Artigo(publicacao=time)
        self.assertIs(pergunta_recente.foi_publicado_recentemente(), True)

    # --- TESTE PARA FUNÇÃO GET_ABSOLUTE_URL()

    def test_get_absolute_url(self):
        id = Artigo(id=1)
        self.assertEqual('/artigo/1/', id.get_absolute_url())


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
        criar_artigo(titulo='Somente um teste',
                     conteudo='Sim, isso eh apenas um teste.')
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['latest'],
                                 ['<Artigo: Somente um teste>'])

    # --- TESTE PARA FUNÇÃO INDEXARTIGO()

    def test_index_artigo_view_primeiro_artigo(self):
        # Se o id corresponde ao primeiro artigo, uma mensagem
        # apropriada deve ser exibida
        criar_artigo(titulo='Somente um teste',
                     conteudo='Sim, isso eh apenas um teste.')
        response = self.client.get(reverse('index_artigo', args=['1']))
        self.assertEqual(response.status_code, 200)
        self.assertIn('/artigo/1/', response.request['PATH_INFO'])

    # --- TESTES PARA FUNÇÃO VIEWARTIGO()

    def test_viewArtigo_params_corretos(self):
        response = self.client.get(
            reverse('artigo', args=['suelensantos', '12', '09', '2016'])
        )
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['msg'], [])

    def test_viewArtigo_params_incorretos(self):
        # kwargs={'titulo': 'suelensantos',
        #         'dia': '12',
        #         'mes': '9',
        #         'ano': '2016'}
        response = self.client.get(
            reverse('artigo', args=['a' * 120, '32', '15', '2052'])
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn('ERRO-01!', response.context['msg'][0])
        self.assertIn('ERRO-02!', response.context['msg'][1])
        self.assertIn('ERRO-03!', response.context['msg'][2])
        self.assertIn('ERRO-04!', response.context['msg'][3])

    # --- TESTES PARA FUNÇÕES VALIDA...()

    # Testes para validar título

    def test_valida_titulo_valido(self):
        titulo_valido = valida_titulo('abcdefghijklmnopqrstuvwxyz')
        self.assertTrue(titulo_valido)

    def test_valida_titulo_invalido(self):
        titulo_invalido = valida_titulo('a' * 120)
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

    # --- TESTES PARA FUNÇÃO CONTATO()

    def test_contato_form_valido(self):

        dados_post = {
            'nome': 'Suelen Santos',
            'email': 'suelensantos@hotmail.com',
            'mensagem': 'Este eh apenas um teste que valida o formulario de contato.'
        }

        response = self.client.get('/contato/')
        self.assertContains(response, '<h2>  Contato  </h2>')
        response = self.client.post('/contato/', dados_post)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Contato enviado!', response.context['mostrar'])

    def test_contato_form_invalido(self):

        dados_post = {
            'nome': 'Suelen Santos',
            'email': 'nao eh um email'
        }

        response = self.client.post('/contato/', dados_post)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response, 'form', 'mensagem', u'Este campo é obrigatório.')
        self.assertFormError(response, 'form', 'email', u'Informe um endereço de email válido.')
