from django.shortcuts import render,redirect
from django.contrib.messages import success
from .models import WeatherNow
from datetime import date
import time



# Create your views here.



def weather_view(request,*args,**kwargs):
    city = ''
    update = None
    samples = WeatherNow.objects.all()[:12]
    if request.method == 'GET':
        city = request.GET.get('search_box',None)
        city = city.capitalize()

    try:
        obj = WeatherNow.objects.get(name=city)
    except WeatherNow.DoesNotExist:
        obj = None

    if obj != None:
        t = time.localtime()
        hold = str(WeatherNow.objects.get(name = "Abuja").weather_time)
        if date.today() == obj.weather_date and time.strftime("%H:%M",t) == hold[0:5]:
            update =  'weather details has been updated'
            success(request, 'weather details haas been updated')

    ip = request.META.get('REMOTE_ADDR', None)
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        print(x_forwarded_for)
    if ip:
        print(ip)



    context = {'object': obj, 'update':update, 'samples': samples }
    return render(request,'pages/home.html',context)
