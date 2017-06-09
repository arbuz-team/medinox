from django.db import models


class Language_EN(models.Model):
    value = models.CharField(max_length=200)

class Language_PL(models.Model):
    value = models.CharField(max_length=200)

class Language_DE(models.Model):
    value = models.CharField(max_length=200)
