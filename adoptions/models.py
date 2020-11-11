from django.db import models
from django.contrib.auth.models import User


class Submitter(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="profile.png", null=True, blank=True)
    description = models.TextField(null=True, blank=True, max_length=1000)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
    
    


class Pet(models.Model):

    SEX_CHOICES = [
        ("Male", "Male"), ("Female", "Female")
    ]

    name = models.CharField(max_length=100)
    submitter = models.ManyToManyField(Submitter, default='SPCA')
    species = models.CharField(max_length=100)
    breed = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    sex = models.CharField(max_length=10, blank=True, choices=SEX_CHOICES)
    submission_date = models.DateTimeField(auto_now_add=True)
    age = models.IntegerField(null=True)
    pet_image = models.ImageField(default="pet_profile.png", null=True, blank=True, upload_to="static/images/")
    #submitter_image = models.ImageField(default="profile.png", null=True, blank=True)
    vaccinations = models.ManyToManyField("Vaccine", blank=True)

    def __str__(self):
        return self.name

class Vaccine(models.Model):

    name = models.CharField(max_length=50) 

    def __str__(self):
        return self.name