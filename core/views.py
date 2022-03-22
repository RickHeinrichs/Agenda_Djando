from django.shortcuts import render, redirect
from core.models import Evento

# Create your views here.

#def index(request):
#   return redirect('/agenda/') #Funcao index para retornar a pagina agenda sempre que chamar a pagina

def lista_eventos(request):
    #usuario = request.user #Pega o usuário que está enviando a requisição
    #evento = Evento.objects.filter(usuario=usuario) #Retorna os eventos do usuario logado
    evento = Evento.objects.all()   #Todos os ID      #get(id=1) Traz apenas um ID escolhido
    dados = {'eventos':evento} #Cria o dicionario dos eventos
    return render(request, 'agenda.html', dados) #Renderiza para a pagina html