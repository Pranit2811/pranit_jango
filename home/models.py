from pickle import TRUE
from django.db import models
from django.db.models.enums import Choices
# Create your models here.
class Form(models.Model):
    id = models.AutoField(primary_key=True)
    Choices1=(('Male',"male"),('Female',"female"))
    Choices2=(('3 Months',"p1"),('6 Months',"p2"),('12 Months',"p3"))
    ename=models.CharField(max_length=150,null=True) 
    email=models.CharField(max_length=150,null=True)
    num=models.CharField(max_length=150,null=True)
    gender=models.CharField(max_length=6,choices=Choices1,default=False)
    address=models.CharField(max_length=150,null=True)
    comment=models.TextField(max_length=150,null=True)
    plans=models.CharField(max_length=9,choices=Choices2,default=False)
    def __str__(self):
        return self.ename
