from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required #Importa a função para autenticação de usuário
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

#def index(request):
#   return redirect('/agenda/') #Funcao index para retornar a pagina agenda sempre que chamar a pagina

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/')
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request,"Usuário ou senha inválido!")
            return redirect('/')

@login_required(login_url='/login/') #Força a ter alguém logado para abrir a pagina
def lista_eventos(request):
    usuario = request.user
    #usuario = request.user #Pega o usuário que está enviando a requisição
    #evento = Evento.objects.filter(usuario=usuario) #Retorna os eventos do usuario logado
    evento = Evento.objects.filter(usuario=usuario)   #Todos os ID      #get(id=1) Traz apenas um ID escolhido
    dados = {'eventos':evento} #Cria o dicionario dos eventos
    return render(request, 'agenda.html', dados) #Renderiza para a pagina html