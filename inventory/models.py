from django.db import models
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    ref_code = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    brand = models.ForeignKey(
        'inventory.Brand', on_delete=models.CASCADE, related_name='brands'
    )
    image = models.ImageField(blank=True, null=True, upload_to='images/')
    discount = models.IntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.brand}"


class Brand(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField(null=True, blank=True)
    logo = models.ImageField(blank=True, null=True, upload_to='images/')
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class Comments(models.Model):
    product = models.ForeignKey(
        'inventory.Product', on_delete=models.CASCADE, related_name='products'
    )
    author = models.CharField(max_length=20)
    text = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text