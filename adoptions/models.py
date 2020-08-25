from django.db import models

# Create your models here.
class Pet(models.Model):

    SEX_CHOICES = [
        ("M", "Male"), ("F", "Female")
    ]

    name = models.CharField(max_length=100)
    subitter = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=1, blank=True, choices=SEX_CHOICES)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    vaccinations = models.ManyToManyField("Vaccine", blank=True)

class Vaccine(models.Model):

    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name