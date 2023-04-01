from django.db import models
from store.models import Store

class Shopping(models.Model): # django의 Model class를 상속받음
    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=50)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    count = models.IntegerField()
    price = models.IntegerField()
    image = models.ImageField(blank=True, upload_to='shopping/')

