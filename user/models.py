from django.db import models
from django.db.models import SET_NULL

class Country(models.Model):
    name = models.CharField(max_length=250)
    country_law = models.TextField()
    country_history = models.TextField()
    to_work = models.BooleanField(default=False)
    to_study = models.BooleanField(default=False)
    work = models.BooleanField(default=False)
    study = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=250)
    country =models.ForeignKey(Country,on_delete=models.CASCADE)
    to_study = models.BooleanField(default=False)
    study = models.BooleanField(default=False)
    work = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Embassy(models.Model):
    name = models.CharField(max_length=250)
    country =models.ForeignKey(Country,on_delete=models.CASCADE)
    location = models.TextField()

    def __str__(self):
        return self.name





class University(models.Model):
    name = models.CharField(max_length=250)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name='universities')
    location = models.CharField(max_length=250)
    country = models.ForeignKey(Country, on_delete=SET_NULL, null=True, related_name='universities')

    def __str__(self):
        return self.name


class WorkCategory(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Work(models.Model):
    category = models.ForeignKey(WorkCategory,on_delete=models.SET_NULL,null=True)
    company_name = models.CharField(max_length=250)
    company_fon_number = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    work_stafka = models.CharField(max_length=250)
    salary = models.CharField(max_length=250)
    dokument = models.CharField(max_length=250)


    def __str__(self):
        return self.position


class User(models.Model):
    chat_id = models.CharField(max_length=255,unique=True)
    full_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=250)
    location =  models.TextField()

    def __str__(self):
        return self.full_name


class Offer(models.Model):
    user = models.CharField(max_length=250)
    offer = models.TextField()

    def __str__(self):
        return str(self.user)


class HomeProblem(models.Model):
    user = models.CharField(max_length=250)
    problem = models.TextField()

    def __str__(self):
        return str(self.user)


