from django.db import models
from django.contrib.auth.models import AbstractBaseUser , PermissionsMixin , BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            email = self.normalize_email(email)
        username = username
        user = self.model(username=username, email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin) :

    USER_ROLES = (
        ("Admin","Admin"),
        ("Developer","Developer"),
        ("Tester","Tester"),
    )

    username   = models.CharField(max_length=255, unique=True)
    email      = models.EmailField(max_length=255, unique=True)
    role       = models.CharField(max_length=255, choices=USER_ROLES)
    is_staff   = models.BooleanField(default=False)
    is_active  = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD  = "email" 
    REQUIRED_FIELDS = ["username", "role"]

class Account(models.Model) :
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='account')
    image= models.ImageField(upload_to='accounts/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
