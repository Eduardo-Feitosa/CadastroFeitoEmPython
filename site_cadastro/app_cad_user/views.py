from django.shortcuts import render
from .models import Usuario
# Create your views here.
def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    #salvar dados da tela para o banco
    novo_usuario = Usuario()
    novo_usuario.nome = request.POST.get('Nome')
    novo_usuario.idade = request.POST.get('Idade')
    novo_usuario.save()
    #Exibir todos os Usuarios já cadastrados em uma nova página
    usuarios ={
        'usuarios':Usuario.objects.all()
    }
    #retornar dados para pagina de usuarios
    return render(request,'usuarios/usuarios.html',usuarios)