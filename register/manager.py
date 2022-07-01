from django.contrib.auth.models import BaseUserManager

class EmployeeManager(BaseUserManager):

    def create_user(self, email, name, password=None):
      
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name = name,
        )
        user.is_active = True
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password=None):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email = email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
