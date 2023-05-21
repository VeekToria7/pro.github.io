from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title= models.CharField(max_length=100)
    picture= models.FileField()

    def __str__(self):
        return self.title

class Product(models.Model):
    picture= models.FileField()
    title= models.CharField(max_length=100)
    price= models.FloatField()
    category= models.ForeignKey(Category, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

class Profile(models.Model):
    address= models.CharField(max_length=200)
    phone_number= models.CharField(max_length=20)
    user= models.OneToOneField(User, on_delete= models.CASCADE)

    def __str__(self):
        return self.title

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title