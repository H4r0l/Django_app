from django.contrib import admin
from .models import Product, Brand, Comment
# Register your models here.

admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Comment)