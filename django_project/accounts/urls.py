from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('sign-up/', views.signup, name='sign-up'),
    path('logout/', views.logout, name='logout'),
]