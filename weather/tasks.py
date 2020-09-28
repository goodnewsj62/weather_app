from __future__ import absolute_import,unicode_literals
from celery import  shared_task
from celery import Celery
from celery.schedules import crontab
from django.contrib.messages import success
from .models import WeatherNow
from urllib import request as req
import json
import os








app = Celery()




@shared_task(name = 'weather_scrapper')
def weather_scrapper(*args,**kwargs):


    key = os.environ.get( 'OPEN_WEATHER_API')
    url = 'https://api.openweathermap.org/data/2.5/find?lat=9&lon=8&cnt=50&exclude=daily,minutely&&appid=' + key
    site = req.urlopen(url).read()
    data = json.loads(site)


    for n in range(len(data['list'])):
        hold = dict()
        hold['name'] = data['list'][n]['name']
        hold['temperature'] = (data['list'][n]['main']["temp"]) - 273
        hold['humidity'] = str(data['list'][n]['main']["humidity"]) + "%"
        hold['description'] = data['list'][n]['weather'][0]["main"]
        icon = data['list'][n]['weather'][0]["icon"]
        name = data['list'][n]['name']
        hold['icon'] = 'http://openweathermap.org/img/wn/'+icon+'@2x'+'.png'
        try:
            obj =WeatherNow.objects.get(name = name)

            for key,value in hold.items():
                setattr(obj,key,value)
            obj.save()
        except WeatherNow.DoesNotExist:
            obj = WeatherNow(name = hold['name'], temperature = hold['temperature'],humidity = hold['humidity'],icon = hold['icon'] )
            obj.save(force_insert= True)







@shared_task(name = 'print_message')
def print_message(name , *args,**kwargs):
    print('CELERY is working!!{}have implemented it correctly.'.format(name))

@shared_task(name = "add")
def add(x,y):
    print("Add function")
    return x+y