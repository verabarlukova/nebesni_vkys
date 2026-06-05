from django.contrib import admin
from .models import Client, Product, Order, Ingredient, Promotion

# Регистрируем каждую модель, чтобы она появилась в админке
admin.site.register(Client)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Ingredient)
admin.site.register(Promotion)