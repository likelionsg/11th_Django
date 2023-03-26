from django.db import models

class Store(models.Model):
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)