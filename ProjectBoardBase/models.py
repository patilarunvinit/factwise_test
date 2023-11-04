from django.db import models




class BoardData(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    team_id=models.IntegerField(null=True)
    creation_time = models.DateField(null=True)
    status = models.CharField(max_length=15,blank=True,default="OPEN")
    end_time = models.DateField(null=True,blank=True)


    objects = models.Manager()




class TaskData(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length=128)
    user_id=models.IntegerField(null=True)
    creation_time = models.DateField(null=True)
    status = models.CharField(max_length=15,blank=True)


    objects = models.Manager()
