from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	t = [('Medicininst','Medicininst'),('Organisation','Organisation'),('None','None')]
	user_type = models.CharField(choices=t,default='None',max_length=15)
	lc_no =  models.ImageField(upload_to='UserCheck/',null=True)
	age = models.IntegerField(null=True)
	pan_no = models.CharField(max_length=10,null=True)
	phone_no = models.CharField(max_length=10,null=True)
	address = models.CharField(max_length=250,null=True)
	p = [(1,'Medicininst'),(2,'Organisation'),(3,'Anonymous')]
	role = models.IntegerField(choices=p,default=3)
