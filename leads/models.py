from django.db import models

# Create your models here.


class Lead(models.Model):
   
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=30)
    age=models.IntegerField(default=0)
    agent=models.ForeignKey("Agent",on_delete=models.CASCADE)

class Agent(models.Model):
    first_name=models.CharField(max_length=40)
    last_name=models.CharField(max_length=30)
  



