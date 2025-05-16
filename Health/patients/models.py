from django.db import models


class patients(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)

class doctors(models.Model):
    firstname = models.CharField(max_length = 255)
    lastname = models.CharField(max_length = 255)