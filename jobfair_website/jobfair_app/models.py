from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 256)

    description = models.TextField(
        default = ' ',
        max_length=500,
    )

    stipend = models.IntegerField(
        default = 0,
     )

    def __str__(self):
        return self.name


class Freelancer(models.Model):
    name = models.CharField(max_length = 256)
    rating = models.IntegerField(
        default = 0,
     )
    project = models.ForeignKey(Project, related_name = 'freelancers', on_delete=models.CASCADE,)

    def __str__(self):
        return self.name


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    #aditional
    rating = models.IntegerField(default = 0,)

    def __str__(self):
        return self.user.username
