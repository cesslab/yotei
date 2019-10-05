from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    MANAGER = 1
    EXPERIMENTER = 2
    SUBJECT = 3
    ROLE = ((MANAGER, 'MANAGER'), (EXPERIMENTER, 'EXPERIMENTER'), (SUBJECT, 'SUBJECT'))

    full_name = models.CharField('full name', max_length=255)
    role = models.PositiveSmallIntegerField('role', choices=ROLE)

