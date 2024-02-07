from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Spcealization(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)
    def __str__(self) -> str:
        return self.name

class Designation(models.Model):
    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=40)
    def __str__(self) -> str:
        return self.name

class AvailableTime(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class Doctor(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="doctor/images")
    designation = models.ManyToManyField(Designation)
    spcealization = models.ManyToManyField(Spcealization)
    availabletime = models.ForeignKey(AvailableTime,on_delete = models.CASCADE)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length = 20)

    def __str__(self) -> str:
        return f"Dr. {self.user.first_name} {self.user.last_name}"