from django.db import models
from django.utils import timezone
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    ref_code = models.CharField(max_length=10)
    category = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True, upload_to='images/')

    discount = models.IntegerField()

    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} | {self.brand}"