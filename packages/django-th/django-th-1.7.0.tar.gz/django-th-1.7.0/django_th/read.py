# coding: utf-8
from __future__ import unicode_literals
from __future__ import absolute_import
# django
from django.conf import settings
from django.utils.timezone import now
# trigger happy
from django_th.services import default_provider
from django_th.models import TriggerService
from django_th.tools import warn_user_and_admin

from logging import getLogger

logger = getLogger('django_th.trigger_happy')


class Read(object):
    """
        Extracting the data from any service
    """
    def provider(self, service_provider, **kwargs):
        """
            get the data of the provider service
            :param service_provider:
            :param kwargs:
            :return:
        """
        getattr(service_provider, '__init__')(kwargs.get('token'))
        return getattr(service_provider, 'read_data')(**kwargs)

    def is_ceil_reached(self, service):
        """
            check if the ceil of nb of tries is reached
        :param service:
        :return:
        """
        failed = service.provider_failed + 1
        if failed > settings.DJANGO_TH.get('failed_tries', 10):
            TriggerService.objects.filter(id=service.id).update(date_result=now(), status=False)
        else:
            TriggerService.objects.filter(id=service.id).update(date_result=now(), provider_failed=failed)

        warn_user_and_admin('provider', service)

    def reading(self, service):
        """
           get the data from the service and put theme in cache
           :param service: service object to read
           :type service: object
        """
        # counting the new data to store to display them in the log provider - the service that offer data
        provider_token = service.provider.token
        default_provider.load_services()
        service_provider = default_provider.get_service(str(service.provider.name.name))
        date_triggered = service.date_triggered if service.date_triggered else service.date_created

        # get the data from the provider service
        kwargs = {'token': provider_token, 'trigger_id': service.id, 'date_triggered': date_triggered}
        data = self.provider(service_provider, **kwargs)

        if len(data) > 0:
            logger.info("{} - {} new data".format(service, len(data)))
        elif data is False:
            # if data is False, something went wrong
            self.is_ceil_reached(service)
