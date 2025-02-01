from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager as BaseUserManager
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class UserManager(BaseUserManager):
    """
    Manager for the user model, provides methods to create user and superuser
    instances.
    """

    def _create_user(
        self,
        related_model_name = None,
        role_data  = None,
        base_data  = None,
        user_type='paciente'
    ) -> "Usuarios":
        """
        This is a private method that handles the creation of a user instance.
        Optionally it can associate to a model instance that encapsulates the user
        role data if related_model_name and role_data are provided.
        """

        related_instance = None

        if related_model_name and role_data:
            related_model = ContentType.objects.get(
                model=related_model_name
            ).model_class()
            related_instance = related_model.objects.create(**role_data)

        email = base_data.pop("email")
        password = base_data.pop("password")
        user: "Usuarios" = self.model(
            email=self.normalize_email(email),
            user_type=user_type,  # Asignar el tipo de usuario

            content_object=related_instance,
            ** base_data,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def pacientes(self,base_data, role_data):
        base_data.setdefault("is_staff", False)
        base_data.setdefault("is_superuser", False)
        base_data.setdefault("is_active", True)
        return self._create_user(
            related_model_name='pacientes',
            role_data=role_data,
            base_data=base_data,
            user_type='paciente'
        )
    
    def doctors(self, base_data, role_data):
        base_data.setdefault("is_staff", False)
        base_data.setdefault("is_superuser", False)
        base_data.setdefault("is_active", True)
        return self._create_user(
            related_model_name='doctors',
            role_data=role_data,
            base_data=base_data,
            user_type='doctor'
        )
    
    def create_user(self, role_data,user_role, base_data):
    
        map_creation_method = {'pacientes': self.pacientes, 'doctors': self.doctors}
        return map_creation_method[user_role](
            role_data=role_data, base_data=base_data
        )
        
    
    def create_superuser(
        self,
        email: str,
        password: str,
        **base_data,
    ):
        """
        Create and save a SuperUser with the given email and password.
        """

        base_data.setdefault("is_staff", True)
        base_data.setdefault("is_superuser", True)
        base_data.setdefault("is_active", True)

        if base_data.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        elif base_data.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        elif base_data.get("is_active") is not True:
            raise ValueError("Superuser must have is_active=True.")

        base_data["email"] = email
        base_data["password"] = password

        return self._create_user(base_data=base_data,user_type='superuser')
    
    
# Create your models here.
class Usuarios(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=10)
    address = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default= False)
    date_joined = models.DateTimeField(auto_now_add=True)    
    objects: UserManager = UserManager()
    
    
    # Campo para identificar el tipo de usuario
    USER_TYPE_CHOICES = (
        ('paciente', 'Paciente'),
        ('doctor', 'Doctor'),
        ('superuser', 'Superusuario'),
    )
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='paciente')

    objects = UserManager()


    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    content_type = models.ForeignKey(
        db_column="content_type",
        to=ContentType,
        on_delete=models.SET_NULL,
        null=True,
    )
    role_data_id = models.IntegerField(
        db_column="role_data_id",
        null=True,
        blank=True,
    )
    content_object = GenericForeignKey(
        ct_field="content_type",
        fk_field="role_data_id",
    )
    
    
class Doctors(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    licence_number = models.BigIntegerField()
    speciality = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    identification_number = models.BigIntegerField(default=0)
    
    
    
class Pacientes(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    identification_number = models.BigIntegerField()
    rh = models.CharField(max_length=5)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    estado_civil = models.CharField(max_length=30)
    