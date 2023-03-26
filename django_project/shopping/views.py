from django.shortcuts import get_object_or_404, render
from .models import Shopping

def shopping_list(request):
    qs = Shopping.objects.all()
    return render(request, 'index.html', {'item_list': qs,})

def detail(request, pk):
    item = get_object_or_404(Shopping, pk=pk)
    return render(request, 'detail.html', {'item':item,})