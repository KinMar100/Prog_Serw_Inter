from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone

# Create your models here.


class Rank(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) -> str:
        return self.name


class CustomUserManager(UserManager):
    """Own User Manager"""
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("No e-mail provided/Non-valid e-mail")
        if not password:
            raise ValueError("No password provided/Non-valid password")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """User model"""
    email = models.EmailField(blank=True, default='', unique=True)
    name = models.CharField(blank=True, max_length=255, default='')
    rank = models.ForeignKey(Rank, on_delete=models.SET_NULL, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_added = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True, blank=True)

    object = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self) -> str:
        return self.name

    def get_short_name(self) -> str:
        return self.name or self.email.split('@')[0]

# done
