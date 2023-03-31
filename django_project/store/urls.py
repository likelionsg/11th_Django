from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_list, name='store_page'),
]