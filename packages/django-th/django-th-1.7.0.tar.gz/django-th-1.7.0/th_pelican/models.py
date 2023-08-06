# coding: utf-8
from django.db import models
from django_th.models.services import Services
from django_th.models import TriggerService


class Pelican(Services):

    """
        pelican model
    """
    title = models.CharField(max_length=80)
    url = models.URLField()
    tags = models.CharField(max_length=200, blank=True)
    category = models.CharField(max_length=200, blank=True)
    path = models.CharField(max_length=255)
    trigger = models.ForeignKey(TriggerService, on_delete=models.CASCADE)

    class Meta:
        app_label = 'th_pelican'
        db_table = 'django_th_pelican'

    def show(self):
        """

        :return: string representing object
        """
        return "My Pelican %s" % self.name

    def __str__(self):
        return '%s' % self.name
