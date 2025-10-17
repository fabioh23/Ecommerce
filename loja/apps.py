from django.apps import AppConfig
from django.contrib.auth import get_user_model


class LojaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loja'

    # def ready(self):
    #     from django.contrib.auth.models import User
    #     from .models import Cliente
    #     import os
    #
    #     email = os.getenv('EMAIL_ADMIN')
    #     senha = os.getenv('SENHA_ADMIN')
    #
    #     usuarios = User.objects.filter(email=email)
    #     if not usuarios:
    #         User.objects.create_superuser(username=email, email=email, password=senha, is_active=True, is_staff=True)
    #
    #     super_user = User.objects.get(email=email, is_staff=True, is_superuser=True)
    #     super_user_id = super_user.pk
    #
    #     User = get_user_model()
    #     user_instance = User.objects.get(pk=super_user_id)
    #     Cliente.user = user_instance
    #     if super_user:
    #         Cliente.objects.create(email=email, usuario=Cliente.user)