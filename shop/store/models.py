from django.db import models

class Product(models.Model):
    name = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='img', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    remain= models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name