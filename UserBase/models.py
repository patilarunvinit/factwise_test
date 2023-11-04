from django.db import models




class userData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    display_name = models.CharField(max_length=64)
    description = models.CharField(max_length=128)
    creation_time = models.DateField(null=True)


    objects = models.Manager()
