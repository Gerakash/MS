from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Dossier(models.Model):
    user = models.OneToOneField(User,on_delete=models.SET_NULL,null=True,related_name='dossier')
    image = models.ImageField(blank=True,null=True)
    date_birth = models.DateField()
    date_join = models.DateField(auto_now_add=True)
    full_name = models.CharField(max_length=100)
    phone = PhoneNumberField()
    address = models.CharField(max_length=100)
    department = models.CharField(choices=(

        ('SF','security_forces'),
        ('AF','air_forces'),
        ('SpF','space_forces'),
        ('MF','marine_forces')
    ),max_length=20)
    experience = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.full_name + '' + self.department


class Car(models.Model):
    car_model = models.CharField(max_length=50)
    mark = models.CharField(max_length=50)
    year = models.PositiveIntegerField(default=0)
    country = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    wheel_type = models.CharField(choices=(
        ('RH','RH'),
        ('LH','LH')), max_length=50)
    car_type = models.CharField(choices=(
        ('service','service'),
        ('private','private')),max_length=100)
    car_number = models.CharField(max_length=10)
    dossier = models.ForeignKey(Dossier,on_delete=models.CASCADE,blank=True,null=True,related_name='cars')



