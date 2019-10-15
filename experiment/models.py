from django.db import models

from users.models import Researcher, Subject


class Experiment(models.Model):
    name = models.CharField(max_length=255)
    researchers = models.ManyToManyField(Researcher)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    # 12052019_12:30pm_1
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}-{}".format(self.datetime.strftime("%b%d%Y-%l%:M%p"), self.pk)


class PrimaryList(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.session


class WaitList(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return self.session



