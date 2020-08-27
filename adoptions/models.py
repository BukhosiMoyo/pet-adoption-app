from django.db import models

# Create your models here.
class Pet(models.Model):

    SEX_CHOICES = [
        ("Male", "Male"), ("Female", "Female")
    ]

    name = models.CharField(max_length=100)
    subitter = models.CharField(max_length=100, null=True, blank=True)
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=10, blank=True, choices=SEX_CHOICES)
    submission_date = models.DateTimeField()
    age = models.IntegerField(null=True)
    pet_image = models.ImageField(default="pet_profile.png", null=True, blank=True, upload_to="static/images/")
    #submitter_image = models.ImageField(default="profile.png", null=True, blank=True)
    vaccinations = models.ManyToManyField("Vaccine", blank=True)

class Vaccine(models.Model):

    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name