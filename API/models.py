from django.db import models

# Create your models here.

class Post_car(models.Model):
    """Nos permite fazer uma nova postagem de carros em aluguel"""
    id_carro = models.AutoField(primary_key=True)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    descricao = models.TextField(max_length=255, null=False)
    p_foto = models.ImageField(null=False, upload_to='static/imagens', blank=True)
    data_publicacao = models.DateTimeField(auto_now_add=True)

    
"""class Aluguel(models.Model):
    Representa os carros alugados"""