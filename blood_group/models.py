import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse, reverse_lazy

# Create your models here.
class Location(models.Model):
	location_name = models.CharField(max_length=200)

	def __str__(self):
		return self.location_name

class Doner(models.Model):
	location = models.ForeignKey(Location,on_delete=models.CASCADE)
	donar_name = models.CharField(max_length=100)
	donar_blood_group = models.CharField(max_length=100)
	mobile_number = models.CharField(max_length=100)

	def __str__(self):
		return self.donar_name
	def get_absolute_url(self):
		return reverse('blood_group:index')
		

