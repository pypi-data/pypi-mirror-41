# coding: utf-8
from django.db import models
from django_th.models.services import Services
from django_th.models import TriggerService


class Github(Services):

    """
        github model to be adapted for the new service
    """
    # put whatever you need  here
    # eg title = models.CharField(max_length=80)
    # but keep at least this one
    repo = models.CharField(max_length=80)  # owner
    project = models.CharField(max_length=80)  # repo
    trigger = models.ForeignKey(TriggerService, on_delete=models.CASCADE)

    class Meta:
        app_label = 'th_github'
        db_table = 'django_th_github'

    def show(self):
        """

        :return: string representing object
        """
        return "My Github %s" % self.name

    def __str__(self):
        return self.name
