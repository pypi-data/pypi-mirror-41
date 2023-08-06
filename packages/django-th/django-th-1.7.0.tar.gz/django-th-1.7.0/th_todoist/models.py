# coding: utf-8
from django.db import models
from django_th.models.services import Services
from django_th.models import TriggerService


class Todoist(Services):

    """
        todoist model to be adapted for the new service
    """
    trigger = models.ForeignKey(TriggerService, on_delete=models.CASCADE)

    class Meta:
        app_label = 'th_todoist'
        db_table = 'django_th_todoist'

    def show(self):
        """

        :return: string representing object
        """
        return "My Todoist %s" % self.name

    def __str__(self):
        return "%s" % self.name
