from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='teams_logos', blank=True, null=True)
    def __str__(self):
        return self.name
