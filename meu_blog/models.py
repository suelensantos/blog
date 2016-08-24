from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Artigo(models.Model):
   titulo = models.CharField(max_length=100)
   conteudo = models.TextField()
   publicacao = models.DateTimeField()

   def foi_publicado_recentemente(self):
	now = timezone.now()
	return now - datetime.timedelta(days=1) <= self.publicacao <= now
   foi_publicado_recentemente.admin_order_field = 'publicacao'
   foi_publicado_recentemente.boolean = True
   foi_publicado_recentemente.short_description = 'Publicado recentemente?'

