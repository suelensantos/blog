from django.shortcuts import render
from .models import Artigo 

# Create your views here.
def index(request):
	latest = Artigo.objects.all() 
	context = {'latest': latest}
	return render(request, 'meu_blog/index.html', context)
