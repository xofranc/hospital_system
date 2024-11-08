from users.models import Usuarios
from django.contrib.auth.backends import ModelBackend


class EmailPasswordBackend(ModelBackend):
    """
    A custom authentication backend that authenticates users based on their email
    and password.
    """


    def authenticate(self, request,  email, password):
        """
        Authenticate a user with the given email and password.
        """

        user = Usuarios.objects.filter(email=email).first()

        if not user:
            return None

        return user if user.check_password(raw_password=password) else None