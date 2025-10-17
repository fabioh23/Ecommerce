from django.apps import AppConfig


class LojaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loja'

    def ready(self):
        from django.contrib.auth.models import User
        from .models import Cliente
        import os

        email = os.getenv('EMAIL_ADMIN')
        senha = os.getenv('SENHA_ADMIN')

        usuarios = User.objects.filter(email=email)
        if not usuarios:
            User.objects.create_superuser(username=email, email=email, password=senha, is_active=True, is_staff=True)

        super_user = User.objects.get(email=email, is_staff=True, is_superuser=True)
        super_user_id = super_user.email
        if super_user:
            Cliente.objects.create(email=email, usuario=super_user_id)