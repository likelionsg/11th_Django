from django.shortcuts import render

def shopping_list(request):
    return render(request, 'index.html')