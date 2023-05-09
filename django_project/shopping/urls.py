from django.urls import path
from . import views

urlpatterns = [
    path('', views.shopping_list, name='list_page'),
    path('<int:pk>/', views.detail, name='detail_page'),
    # html form 을 이용해 쇼핑 아이템(Shopping) 객체 만들기
    path('create/', views.create, name='create'),
    # django form을 이용해 쇼핑 아이템(Shopping) 객체 만들기
    path('formcreate/', views.formcreate, name='formcreate'),
    # django modelform을 이용해 쇼핑 아이템(Shopping) 객체 만들기
    path('modelformcreate/', views.modelformcreate, name='modelformcreate'),
    path('search/', views.search, name='search_item'),
]