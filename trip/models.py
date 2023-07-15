from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Master(models.Model):
    created_user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    created_date=models.DateField(null=True)
    class Meta:
        abstract=True

class personal_info(Master):
    student=models.CharField(max_length=100)
    def __str__(self):
        return self.student

