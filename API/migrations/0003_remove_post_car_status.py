# Generated by Django 5.1.2 on 2024-10-29 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_post_car_delete_carro'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_car',
            name='status',
        ),
    ]