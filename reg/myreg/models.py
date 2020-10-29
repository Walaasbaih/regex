from django.db import models
import re 
# Create your models here.
class Reg(models.Model):
    expression= models.CharField(max_length=120 ,default='SOME STRING')
    text = models.CharField(max_length=120 ,default='SOME STRING')
    
    def __str__(self):
        return self.input1
    
