from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    under_30_minute = models.BooleanField(default=False)
    posted_by = models.CharField(max_length=100)
    description = models.TextField()
    instruction = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
