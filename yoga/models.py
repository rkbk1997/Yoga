from django.db import models

# Create your models here.
class routen(models.Model):
    course=models.CharField(max_length=300,null=True,blank=True)
    mon=models.CharField(max_length=300,null=True,blank=True)
    tue=models.CharField(max_length=300,null=True,blank=True)
    wed=models.CharField(max_length=300,null=True,blank=True)
    thu=models.CharField(max_length=300,null=True,blank=True)
    fri=models.CharField(max_length=300,null=True,blank=True)
    sat=models.CharField(max_length=300,null=True,blank=True)
    sun=models.CharField(max_length=300,null=True,blank=True)
    def __str__(self):
            return self.course

class about(models.Model):
    des=models.CharField(max_length=3000,null=True ,blank=True)

class feedback(models.Model):
    pic=models.FileField(null=True ,blank=True)
    des=models.CharField(max_length=30000,null=True,blank=True)
    name=models.CharField(max_length=300,null=True,blank=True)
    post=models.CharField(max_length=300,null=True ,blank=True )

class classes(models.Model):
    pic=models.FileField(null=True,blank=True)
    cname=models.CharField(max_length=300,null=True,blank=True)

class contactme(models.Model):
    address=models.CharField(max_length=3000,null=True ,blank=True)
    ph1=models.CharField(max_length=20,null=True,blank=True)
    ph2=models.CharField(max_length=20,null=True,blank=True)

class trainerdata(models.Model):
    pic=models.FileField(null=True ,blank=True)
    name=models.CharField(max_length=300,null=True,blank=True)
    post=models.CharField(max_length=300,null=True ,blank=True )
