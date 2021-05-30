from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.utils import timezone
# Create your models here.

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    seller_id = models.ForeignKey(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=400)
    price = models.FloatField()
    discount = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='pics')

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=CASCADE)
    product_id = models.ForeignKey(Product,on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    time = models.DateTimeField(default=timezone.now)
    cost = models.FloatField()
    #delivery date

    def __str__(self):
        return self.product_id

class Cart(models.Model):
    order_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=CASCADE)
    prodect_id = models.ForeignKey(Product,on_delete=CASCADE)
    quantity = models.PositiveIntegerField()
    cost = models.FloatField()

    def __str__(self):
        return str(self.order_id)
    



class Address(models.Model):
    address_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=CASCADE)
    pincode = models.IntegerField()
    colony = models.CharField(max_length=40)
    district = models.CharField(max_length=40)
    state = models.CharField(max_length=40)