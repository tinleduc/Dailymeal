import binascii
import os

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.


class User(AbstractUser):
    username = models.CharField(max_length=128)
    email = models.EmailField(_('email address'), blank=True, null=True, unique=True)
    user_type = models.IntegerField(default=1)
    status = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        db_table = 'user'

    def __str__(self):
        return 'User: {}'.format(self.username)
