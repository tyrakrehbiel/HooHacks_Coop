from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Notes(models.Model):
    courseName = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    noteFile = models.FileField(upload_to = 'notes/')
    created_by = models.CharField(max_length=30, default='Anonymous User')
    # user = models.OneToOneField(User, on_delete = models.CASCADE)


    def __str__(self):
        return "Course Name: " + self.courseName + " Topic: " + self.topic

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    pfp = models.ImageField(default='default.jpg',upload_to='profile_pics')
    bio = models.TextField(default='I\'m ready to learn!', max_length=500)
    earnings = models.IntegerField()

    def __str__(self):
        return f'{self.user.username} Profile'
