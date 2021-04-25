from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
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

    upvote = models.IntegerField(
        default = 0,
    )

    downvote = models.IntegerField(
        default = 0,
    )

    skills = models.TextField(
    default = '',
    max_length = 500
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("jobfair_app:project_detail", kwargs = {'pk':self.pk})


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
    description = models.CharField(
               default = '',
               max_length = 200
               )

    class Role(models.TextChoices):
        FREELANCER = 'freelancer', _('freelancer')
        EMPLOYER = 'employer', _('employer')

    role=models.CharField(
        max_length=100,
        choices=Role.choices,
        default=Role.FREELANCER,
    )
    project = models.ForeignKey(Project, related_name = 'users', on_delete=models.CASCADE,default = 1)

    def __str__(self):
        return self.user.username
