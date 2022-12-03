from django.http import HttpResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import Http404, HttpResponseForbidden, JsonResponse
from .models import Palavra, PalavraUsuario
from .serializers import PalavraSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

def index(request):
    return HttpResponse("Olá mundo! Este é o app vocab de Tecnologias Web do Insper.")

@api_view(['GET', 'POST'])  
def api_palavra(request, palavra_id):
    try:
        if palavra_id == 'rand':
            palavra = Palavra.objects.order_by('?').first()
            if PalavraUsuario.objects.filter(palavra=palavra).exists():
                PalavraUsuario.objects.filter(palavra=palavra).add(request.user)
            elif PalavraUsuario.objects.filter(user=request.user).exists():
                PalavraUsuario.objects.filter(user=request.user).add(palavra=palavra)
            else:
                PalavraUsuario.objects.create(user=request.user, palavra=palavra)
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

@api_view(['GET', 'POST', 'DELETE'])
def api_palavras(request):
    try:
        all_palavras = Palavra.objects.all()
    except Palavra.DoesNotExist:
        raise Http404()

    if request.method == 'POST':
        new_palavra_data = request.data
        new_palavra = Palavra(palavra = new_palavra_data['palavra'])
        new_palavra.save()
        all_palavras = Palavra.objects.all()
    if request.method == 'DELETE':
        all_palavras = Palavra.objects.all()
        all_palavras.delete()

    serialized_palavra = PalavraSerializer(all_palavras, many=True)
    return Response(serialized_palavra.data)

@api_view(['POST'])
def api_get_token(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            user = authenticate(username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()


@api_view(['POST'])
def api_cadastro(request):
    try:
        if request.method == 'POST':
            username = request.data['username']
            password = request.data['password']
            user = User.objects.create_user(username=username, password=password)
            user = authenticate(username=username, password=password)

            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({"token":token.key})
            else:
                return HttpResponseForbidden()
    except:
        return HttpResponseForbidden()