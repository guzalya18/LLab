from django.db import models

# Create your models here.


class User(models.Model):
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)


class Teacher(models.Model):
    Name = models.CharField(max_length=50)
    mobile = models.IntegerField()
    special = models.CharField(max_length=50)


class Student(models.Model):
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    mobile = models.IntegerField()

