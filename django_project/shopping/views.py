from django.shortcuts import render
from .models import Shopping

def shopping_list(request):
    qs = Shopping.objects.all()
    return render(request, 'index.html', {'item_list': qs,})