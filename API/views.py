from django.shortcuts import render
from django.http import HttpResponse
from .models import Post_car


def home(request):
    """Rota - Página principal"""
    return render(request, 'home.html')


def viaturas(request):
    """Visualização de viaturas"""
    carros = Post_car.objects.all()

    new_carro = {
        'novo_carro': carros
    }

    return render(request, 'viaturas.html', new_carro)

def carrinho(request):
    """Página que lista todos os itens da compra ou aluguel e o total, factura resumidamente"""
    return render(request, 'carrinho.html')
    pass

def checkout(request):
    """Para fazer o pagamento"""
    pass