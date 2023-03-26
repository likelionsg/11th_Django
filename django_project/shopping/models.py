from django.db import models

class Shopping(models.Model): # django의 Model class를 상속받음
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)
    store = models.CharField(max_length=100)
    count = models.IntegerField()
    price = models.IntegerField()

