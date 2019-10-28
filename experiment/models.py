from django.db import models

from users.models import CustomUser


class Experiment(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    experiment = models.ForeignKey(Experiment, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    num_primary = models.IntegerField()
    num_wait = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "EID:{} Date:{} Time:{} SID:{}".format(
            self.experiment.pk, self.datetime.strftime("%m/%d/%Y"), self.datetime.strftime("%l:%M%p"), self.pk)


class MainList(models.Model):
    session = models.OneToOneField(Session, related_name='main_list', on_delete=models.CASCADE)

    def __str__(self):
        return "Session {} - Main List".format(self.session)


class WaitList(models.Model):
    session = models.OneToOneField(Session, related_name='wait_list', on_delete=models.CASCADE)

    def __str__(self):
        return "Session {} - Wait List".format(self.session)


class Subject(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    wait_lists = models.ManyToManyField(WaitList)
    main_lists = models.ManyToManyField(MainList)

    def __str__(self):
        return self.user.full_name


class Researcher(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    experiments = models.ManyToManyField(Experiment)

    def __str__(self):
        return self.user.full_name



