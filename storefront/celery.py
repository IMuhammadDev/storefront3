from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "storefront.settings")

celery = Celery("sotrefront")
celery.config_from_object("django.conf:settings", namespace="CELERY")
celery.autodiscover_tasks()
