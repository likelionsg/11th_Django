from django.contrib import admin
from .models import Shopping

class ShoppingAdmin(admin.ModelAdmin):
    pass

admin.site.register(Shopping, ShoppingAdmin)
