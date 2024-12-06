from django.shortcuts import render
from django.http import HttpResponse
from .models import Post_car
#from .admin import Post_car


def home(request):
    """Rota - Página principal"""
    carros = Post_car.objects.all().values()

    new_carro = {
        'novo_carro': carros
    }

    return render(request, 'home.html', new_carro)

def viaturas(request):
    """Visualização de viaturas"""
    pass

def checkout(request):
    """Para fazer o pagamento"""
    pass