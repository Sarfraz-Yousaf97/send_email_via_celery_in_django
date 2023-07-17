from __future__ import absolute_import, unicode_literals
import os

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_task.settings')

app = Celery('django_task')
app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Karachi')

app.config_from_object(settings, namespace='CELERY')

# Celery Beat Task

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f"Requests, {self.request!r}")