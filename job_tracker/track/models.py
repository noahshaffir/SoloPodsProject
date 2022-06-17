from django.db import models
from django import *
from django.contrib.auth.models import User
from django.db.models.fields import *
from django.template.defaultfilters import slugify
import datetime
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=False, default="John")
    last_name = models.CharField(max_length=100, blank=False, default="Doe")
    bio = models.TextField(max_length=500, blank=True)
    portfolio_url = models.URLField(max_length=350, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
         ordering = ['-date_created']

    def __str__(self):
        return "User_{}|{} {}".format(self.user, self.first_name, self.last_name)

class Application(models.Model):

    company = models.CharField(max_length=100, blank=False, default="LCS")
    position = models.CharField(max_length=100, blank=False, default="Developer")
    date_applied = models.DateField()
    resume = models.URLField(max_length=350, blank=True) #change to file upload if time permits
    cover_letter = models.URLField(max_length=350, blank=True) #change to file upload if time permits
    class Meta:
         ordering = ['-date_applied']
    # def __str__(self):
    #     return f"""Company: {self.company}
    #     Position: {self.position}
    #     Date applied: {self.date_applied}
    #     Resume: {self.resume}
    #     Cover letter: {self.cover_letter}
    #     """
    