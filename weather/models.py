from django.db import models

# Create your models here.
class WeatherNow(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, default='null')
    temperature = models.DecimalField(decimal_places=3, max_digits= 100)
    humidity = models.CharField(max_length=50)
    icon = models.URLField(max_length=200)
    weather_date = models.DateField(auto_now= True)
    weather_time = models.TimeField(auto_now= True)

