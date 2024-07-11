import random
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django_jalali.db import models as jmodels
from django.utils.translation import gettext_lazy as _
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, fullname, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, fullname=fullname, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, fullname, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, fullname, password, **extra_fields)


class CustomUser(PermissionsMixin, AbstractBaseUser):
    email = models.EmailField(_("email address"), blank=True, null=True, unique=True)
    fullname = models.CharField(max_length=150, default='No Name', verbose_name='نام')
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['fullname']

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserModel(CustomUser):
    is_active = models.BooleanField(default=False)
    ban = models.BooleanField(default=False)
    profile_image = models.ImageField('user/profiles', blank=True, null=True)
    register_date = jmodels.jDateTimeField(auto_now_add=True)
    birth_date = jmodels.jDateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.email} - {self.fullname}'
