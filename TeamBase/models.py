from django.db import models
from django.db.models import IntegerField, Model, CharField
from django_mysql.models import ListTextField



class TeamData(Model):
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    admin = models.CharField(max_length=64)
    creation_time = models.DateField(null=True)
    users=ListTextField(
        base_field=IntegerField(),
        size=50,
    )


    objects = models.Manager()