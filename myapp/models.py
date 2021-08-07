from django.db import models
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser, PermissionsMixin):
    first_name = models.CharField(_('first name'), max_length=30, blank=True,null=True)
    last_name = models.CharField(_('last name'), max_length=150,blank=True,null=True)
    email = models.EmailField(_('email address'), unique=True)
    phone_no = PhoneNumberField(unique=True, null=True)
    
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_superuser = models.BooleanField(_('superuser'), default=False)
    is_active = models.BooleanField(_('active'), default=True)



    def __str__(self):
        return "{}".format(self.email)