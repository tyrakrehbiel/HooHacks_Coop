from django.db import models

# Create your models here.
class Notes(models.Model):
    courseName = models.CharField(max_length=100)
    topic = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    noteFile = models.FileField(upload_to = 'notes/')

    def __str__(self):
        return "Course Name: " + self.courseName + " Topic: " + self.topic
