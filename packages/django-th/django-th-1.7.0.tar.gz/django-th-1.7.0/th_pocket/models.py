# coding: utf-8
from django.db import models
from django_th.models.services import Services
from django_th.models import TriggerService


class Pocket(Services):
    """

        Pocket model to store how you want
        to store url in your account

    """
    tag = models.CharField(max_length=80, blank=True)
    url = models.URLField(max_length=255)
    title = models.CharField(max_length=80, blank=True)
    tweet_id = models.CharField(max_length=80, blank=True)
    trigger = models.ForeignKey(TriggerService, on_delete=models.CASCADE)

    class Meta:
        app_label = 'th_pocket'
        db_table = 'django_th_pocket'

    def show(self):
        """

        :return: string representing object
        """
        return "My Pocket %s" % self.url

    def __str__(self):
        return "%s" % self.url
