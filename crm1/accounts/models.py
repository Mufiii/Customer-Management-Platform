from django.db import models

# Create your models here.

class Customer(models.Model) :
  name = models.CharField(max_length=255, null=True)
  Phone = models.CharField(max_length=255, null=True)
  email = models.CharField(max_length=255, null=True)
  Created_at = models.DateField(auto_now_add=True, null=True)

  def __str__(self) :
    return self.name
  
class Tag(models.Model) :
  name = models.CharField(max_length=25, null=True)
  
  def __str__(self) :
    return self.name
  
class Product(models.Model):
  CATEGORY = (
          ('Indoor','Indoor'),
          ('Out Door','Out Door'),
          )
  name = models.CharField(max_length=50, null=True)
  price = models.FloatField(null=True)
  Category = models.CharField(max_length=50,null=True , choices=CATEGORY)
  description = models.CharField(max_length=250,null=True ,blank=True)
  date_created = models.DateTimeField(auto_now_add=True , null=True)
  tags = models.ManyToManyField(Tag)
 
  def __str__(self) :
    return self.name
  
class Orders(models.Model) :
  STATUS = (
          ('Pending','Pending'),
          ('Out for delivery','Out for delivery'),
          ('Delivered','Delivered'),
          )
  
  customer = models.ForeignKey( Customer, null=True, on_delete=models.SET_NULL)
  product = models.ForeignKey( Product, null=True, on_delete=models.SET_NULL)
  date_created = models.DateTimeField(auto_now_add=True , null=True)
  status = models.CharField(max_length=50,null=True, choices=STATUS)
  
  def __str__(self) :
    return self.name
  