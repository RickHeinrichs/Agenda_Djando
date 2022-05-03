from django.db import models
from django.contrib.auth.models import User #Importa os usuários cadastrados no Django

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento') #Força o nome no lista
    data_criacao = models.DateTimeField(verbose_name='Data de Criação', auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) #Cria uma cascata de escolha dos usuários do Django

    class Meta:
        db_table = 'evento' #Força o nome da tabela ser este.

    def __str__ (self):  #Retorna o nome do evento na lista
        return self.titulo

    def get_data_evento(self):
        return self.data_evento.strftime('%A - %d/%m/%y - %H:%M') #Coloca a data no padrão brasileiro

    def get_data_input_evento(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M') #Converte para o padrao aceito pelo navegador