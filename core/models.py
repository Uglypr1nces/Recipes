from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Sight(models.Model):
    id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100, null=False, blank=False)
    posted_by = models.CharField(max_length=100, null=False, blank=False)
    date = models.CharField(max_length=100, null=False, blank=False)
    sas_amount = models.IntegerField(default=1, null=False, blank=False)
    description = models.CharField(max_length=50, null=False, blank=False)
    def __str__(self):
        return self.location
