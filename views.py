#!usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django import forms
import MySQLdb

# ***** IMPORTANTE ******
# Criar uma tabela
# Com os campos nome, email, mensagem
# E na função enviar(), return chamando
# o banco para salvar os dados

# conectar ao banco mysql
db = MySQLdb.connect(host="localhost", user="root", passwd="", db="db_blog")

cursor = db.cursor()


class FormContato(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    mensagem = forms.Field(widget=forms.Textarea)

    add_contact = ("INSERT INTO contato "
                   "(id, nome, email, mensagem) "
                   "VALUES (%(id)s, %(nome)s, %(email)s, %(mensagem)s")

    # Inserir informações do contato
    data_contact = {
        'id': 1,
        'nome': nome,
        'email': email,
        'mensagem': mensagem,
    }

    def enviar(self):
        return cursor.execute(self.add_contact, self.data_contact)


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
    return render(request, 'contato.html', context)


# Ter certeza de que os dados foram comitados no banco
db.commit()

# cursor.close()
db.close()
