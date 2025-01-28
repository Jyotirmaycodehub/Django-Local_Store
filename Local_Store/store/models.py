# from django.db import models

# # Create your models here.

# class Category(models.Model):
#     name = models.charField(max_length=100)

#     def __str__(self):
#         return self.name
    

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name

# class Product(models.Model):
#     name =models.CharField(max_length=100)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2, decimal_dgitts=10)
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)
#     stock = models.IntegerField()

#     def __str__(self):
#         return self.name

# class Order(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.IntegerField()
#     ordered_at = models.DataTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"Order of {self.quantity} {self.product.name}"        