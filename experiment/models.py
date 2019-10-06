from django.db import models

from users.models import Researcher, Subject


class Experiment(models.Model):
    name = models.CharField(max_length=255)
    researchers = models.ManyToManyField(Researcher)

    def __str__(self):
        return self.name


class Session(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)


class SessionList(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)
