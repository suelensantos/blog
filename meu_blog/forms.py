from django import forms


class FormContato(forms.Form):
    nome = forms.CharField(max_length=50)
    email = forms.EmailField(required=True)
    mensagem = forms.Field(widget=forms.Textarea)

    def enviar(self):
        return 'Contato enviado!'
