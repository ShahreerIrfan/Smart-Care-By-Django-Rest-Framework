from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Patient(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    image = models.ImageField(upload_to="patient/images")
    mobile_no = models.CharField(max_length=12)

    def __str__(self) -> str:
        return f"{self.user.first_name} {self.user.last_name}"
STAR_CHOICES = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐')
]    
# class Review(models.Model):
#     reviewer = models.ForeignKey(Patient,on_delete=models.CASCADE)
#     doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
#     body = models.TextField()
#     created = models.DateTimeField(auto_now_add=True)
#     rating = models.CharField(choices = STAR_CHOICES)


