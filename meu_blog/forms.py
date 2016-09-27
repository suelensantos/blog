from django import forms
from .models import Contato


class FormContato(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    mensagem = forms.Field(widget=forms.Textarea)

    def enviar(self):
        c = Contato(nome=self.data.get("nome"), email=self.data.get("email"), mensagem=self.data.get("mensagem"))
        c.save()
        return 'Contato enviado!'
