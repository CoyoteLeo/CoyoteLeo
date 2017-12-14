from django.db import models


class Experience(models.Model):
    title = models.TextField(blank=False, unique=True)
    description = models.TextField(blank=False)
    image = models.ImageField(blank=True)
    time = models.TextField(blank=False)
    ps = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Ability(models.Model):
    title = models.TextField(blank=False, unique=True)
    description = models.TextField(blank=False)
    time = models.TextField(blank=False)
    ps = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Work(models.Model):
    title = models.TextField(blank=False, unique=True)
    description = models.TextField(blank=False)
    image = models.ImageField(upload_to='image/images_work',blank=True)
    time = models.TextField(blank=False)
    ps = models.TextField(blank=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name=models.TextField(blank=False)
    email=models.EmailField(blank=True)
    message=models.TextField(blank=False)
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
# Create your models here.
