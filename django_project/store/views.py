from django.shortcuts import render
from .models import Store

def store_list(request):
     qs = Store.objects.all()
     return render(request, 'store.html', {'store_list': qs,})
