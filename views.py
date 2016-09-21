from django.shortcuts import render_to_response
from django.template import RequestContext


# verificar um modo de fazer essa parte
# igual ao indexArtigo da outra view (do blog)
# verificar o mesmo na pág 60


def contato(request):

    return render_to_response('contato.html', locals(), context_instance=RequestContext(request))