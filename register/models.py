from register.manager import EmployeeManager
from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class RegisterUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    is_jobsekeer = models.BooleanField(default=False)
    is_jobposter = models.BooleanField(default=False)
    objects = EmployeeManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        
        return self.is_admin