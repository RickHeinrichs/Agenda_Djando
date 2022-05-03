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

@login_required(login_url='/login/') #Solicita o login
def evento(request):
    id_evento = request.GET.get('id')
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request,'evento.html', dados)

@login_required(login_url='/login/') #Solicita o login
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            evento = Evento.objects.get(id=id_evento)
            if evento.usuario == usuario:
                evento.titulo = titulo
                evento.descricao = descricao
                evento.data_evento = data_evento
                evento.save() #Realiza a alteração e salva ao final
            #.update(titulo=titulo,
             #                                           data_evento=data_evento,
              #                                           descricao=descricao)
        else:
            Evento.objects.create(titulo=titulo,
                data_evento=data_evento,
                descricao=descricao,
                usuario=usuario)

    return redirect('/')

@login_required(login_url='/login/') #Solicita o login
def delete_evento(request,id_evento):
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario:
        evento.delete()
    return redirect('/')