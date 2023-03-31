from django.shortcuts import get_object_or_404, render, redirect
from .models import Shopping
from store.models import Store

def shopping_list(request):
    qs = Shopping.objects.all()
    return render(request, 'index.html', {'item_list': qs,})

def detail(request, pk):
    item = get_object_or_404(Shopping, pk=pk)
    return render(request, 'detail.html', {'item':item,})

# 쇼핑 아이템(Shopping) 작성 html을 보여주거나 저장해주는 함수
def create(request):
    if(request.method == 'POST'):
        item = Shopping()
        item.name = request.POST['name']
        item.price = request.POST['price']
        item.count = request.POST['count']
        store_name = request.POST['store']
        item.store = get_object_or_404(Store, name=store_name)
        item.save()
    return render(request, 'create.html')