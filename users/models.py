from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    MANAGER = 1
    RESEARCHER = 2
    SUBJECT = 3
    ROLE = ((MANAGER, 'MANAGER'), (RESEARCHER, 'RESEARCHER'), (SUBJECT, 'SUBJECT'))

    full_name = models.CharField('full name', max_length=255)
    role = models.PositiveSmallIntegerField('role', choices=ROLE)


class Manager(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.full_name


