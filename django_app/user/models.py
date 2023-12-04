from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.

class UserManagement(BaseUserManager):
    def create_user(self, email, password=None, **ext_fields):

        if not email:
            raise ValueError("You have not added an email address for the user")

        user: "User" = self.model(email=self.normalize_email(email), **ext_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Rank(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()


class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    rank = models.ForeignKey(Rank, null=True, on_delete=models.SET_NULL)
    objects = UserManagement()

    USERNAME_FIELD = 'email'
