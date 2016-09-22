#!usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django import forms
from django.core.mail import send_mail
from meu_blog.models import Artigo

# verificar um modo de fazer essa parte
# igual ao indexArtigo da outra view (do blog)
# verificar o mesmo na pág 60


class FormContato(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    mensagem = forms.Field(widget=forms.Textarea)

    def enviar(self):
        titulo = 'Mensagem enviada pelo site'
        destino = 'suelen_cordeiro@hotmail.com'
        texto = """
        Nome: %(nome)s
        E-mail: %(email)s
        Mensagem: %(mensagem)s
        """ % self.cleaned_data

        send_mail(
            subject=titulo,
            message=texto,
            from_email=destino,
            recipient_list=[destino],
        )


def contato(request):
    if request.method == 'POST':
        form = FormContato()

        if form.is_valid():
            form.enviar()
            mostrar = 'Contato enviado!'
            form = FormContato()
    else:
        form = FormContato()

    artigo = Artigo.objects.all()
    context = {'artigo': artigo, 'mostrar': mostrar}
    return render(request, 'contato.html', context)
