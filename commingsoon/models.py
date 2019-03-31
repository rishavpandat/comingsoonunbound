from django.db import models
from django.urls import reverse
from datetime import datetime

class SoonModel(models.Model):
    name = models.CharField(max_length=200)
    business_name = models.CharField(max_length=300, blank=True)
    number = models.CharField(max_length=15)
    email = models.EmailField()
    contact_date = models.DateTimeField(default=datetime.now, blank=True)



    def __str__(self):
        return self.name +'-'+ self.email