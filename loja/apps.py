from django.apps import AppConfig


class LojaConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'loja'

    def ready(self):
        from django.contrib.auth import get_user_model
        import os

        email = os.getenv('EMAIL_ADMIN')
        senha = os.getenv('SENHA_ADMIN')

        users = get_user_model()
        usuarios = users.objects.filter(email=email)
        if not usuarios:
            users.objects.create_superuser(username="admin", email=email, password=senha, is_active=True, is_staff=True)
