from __future__ import absolute_import
from celery import Celery

import os

url = None

os.environ.setdefault('DJANGO_SETTINGS_MODULE','weather_app.settings')
app = Celery('weather_app')

app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'add-every-2-seconds':{
        'task':'weather_scrapper',
        'schedule':60,



    }
}

@app.task(bind = True)
def debug_task(self):
    print('Request:{0!r}'.format(self.request))
