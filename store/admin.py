from django.contrib import admin
from .models import Category, Product, Profile, Cart

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Profile)
admin.site.register(Cart)