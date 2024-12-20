# Generated by Django 5.1.2 on 2024-10-25 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post_car',
            fields=[
                ('id_carro', models.AutoField(primary_key=True, serialize=False)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=12)),
                ('descricao', models.TextField(max_length=255)),
                ('status', models.BooleanField()),
                ('p_foto', models.ImageField(upload_to='')),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Carro',
        ),
    ]
