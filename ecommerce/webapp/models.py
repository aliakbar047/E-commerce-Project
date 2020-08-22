from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class Company(models.Model):
    company_owner = models.ForeignKey(User, on_delete= models.CASCADE)
    company_name = models.CharField(max_length= 100)
    company_category = models.ForeignKey(Category, on_delete= models.CASCADE)
    image = models.ImageField()

    def __str__(self):
        return self.company_name

class Product(models.Model):
    product_name = models.CharField(max_length= 100)
    price = models.IntegerField()
    image = models.ImageField()
    company = models.ForeignKey(Company, on_delete = models.CASCADE)

    def __str__(self):
        return self.product_name


    
