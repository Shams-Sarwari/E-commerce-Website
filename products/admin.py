from django.contrib import admin
from .models import Tag, Product
# Register your models here.

admin.site.register(Product)
admin.site.register(Tag)