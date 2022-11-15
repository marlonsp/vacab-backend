from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from .models import Palavra
from .serializers import PalavraSerializer

def index(request):
    return HttpResponse("Olá mundo! Este é o app notes de Tecnologias Web do Insper.")

@api_view(['GET', 'POST'])
def api_palavra(request, palavra_id):
    try:
        if palavra_id == 'rand':
            palavra = Palavra.objects.order_by('?').first()
        else:
            palavra = Palavra.objects.get(id=int(palavra_id))
    except Palavra.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_palavra_data = request.data
        palavra.palavra = new_palavra_data['palavra']
        palavra.save()

    serialized_palavra = PalavraSerializer(palavra)
    return Response(serialized_palavra.data)