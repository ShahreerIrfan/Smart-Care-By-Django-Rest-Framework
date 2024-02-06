from django.db import models

# Create your models here.
class ContacUs(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length=12)
    problem = models.TextField()

    def __str__(self) -> str:
        return self.name