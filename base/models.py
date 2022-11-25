from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models import Model


class profile(AbstractUser):
    gend = (('Male', 'Male'), ('Female', 'Female'))
    username = models.CharField(unique=True, max_length=200)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(unique=True, max_length=20, default='+234')
    gender = models.CharField(max_length=20, choices=gend, default="male")
    pending_wallet = models.FloatField(default=0.0)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return str(self.username)


class propertise(models.Model):
    author = models.ForeignKey(profile, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    propertise_headline = models.CharField(max_length=300)
    name = models.CharField(max_length=1000, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    price = models.CharField(max_length=200, blank=True, null=True)
    total_bedroom = models.IntegerField(blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    map_location = models.CharField(max_length=300, blank=True, null=True)
    purpose = models.CharField(max_length=200, null=True, blank=True)

    squar_ft = models.CharField(max_length=200, blank=True, null=True)
    bathroom = models.IntegerField(null=True)

    def __str__(self):
        return str(self.name)


class propertiseimg(models.Model):
    name = models.ForeignKey(propertise, on_delete=models.CASCADE)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.name) + " " + str(self.image)


class amenities(models.Model):
    img = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
