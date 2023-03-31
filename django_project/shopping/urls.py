from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_list, name='list_page'),
    path('<int:pk>/', views.detail, name='detail_page'),
]