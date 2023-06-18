from django.db import models
import uuid


class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    tags = models.ManyToManyField('Tag')
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title

class Image(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    img = models.ImageField(blank=True, null=True, default='default.jpg')
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.title



class Tag(models.Model):
    title = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title 

class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return self.title