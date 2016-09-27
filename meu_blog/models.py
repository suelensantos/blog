#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.db import models
import datetime
from django.utils import timezone

# Create your models here.


class Artigo(models.Model):

    class Meta:
        ''' o '-' na frente de publicacao eh usado para
        colocar a lista em ordem decrescente '''
        ordering = ('-publicacao',)

    titulo = models.CharField(max_length=100)
    conteudo = models.TextField()
    publicacao = models.DateTimeField('data de publicação')

    def __unicode__(self):
        return self.titulo

    def foi_publicado_recentemente(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.publicacao <= now

    foi_publicado_recentemente.admin_order_field = 'publicacao'
    foi_publicado_recentemente.boolean = True
    foi_publicado_recentemente.short_description = 'Publicado recentemente?'


class Contato(models.Model):

    nome = models.CharField(max_length=50)
    email = models.EmailField('E-mail')
    mensagem = models.TextField()
