# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.urls import reverse

# Create your models here.

class Celebrity(models.Model):

    name = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    hair_color = models.CharField(max_length=10)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.FileField(upload_to="celebrities/")

    def get_absolute_url(self):
        return reverse('celebrity-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name

