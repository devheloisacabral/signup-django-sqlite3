from django.shortcuts import render
from .models  import Users_table

def home(request):
    return render(request, 'users/home.html')

def users(request):
    #salvando os dados da tela para o banco de dados
    new_user = Users_table()
    new_user.name = request.POST.get('name')
    new_user.age = request.POST.get('age')
    new_user.save()

    #exibindo os dados do banco em uma nova pagina
    usuarios = {
        'usuarios': Users_table.objects.all()
    }

    #retornar os dados que pegamos dentro do dicionario
    return render(request, 'users/users.html', usuarios)