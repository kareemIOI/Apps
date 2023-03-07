from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 120)
    description = models.TextField(null = True, blank = True)
    