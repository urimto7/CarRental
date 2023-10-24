from django.db import models

class Products(models.Model):
    product_id=models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=50, null=True,blank=True)
    product_price=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    product_image=models.ImageField(upload_to="media/products", null=True,blank=True)
    product_text=models.TextField(max_length=300 ,null=True,blank=True)

    def __str__(self):
        return f"{self.product_name}"


class Orders(models.Model):
    product=models.CharField(max_length=50, null=True,blank=True)
    name=models.CharField(max_length=50, null=True,blank=True)
    email=models.EmailField(max_length=254,null=True,blank=True)   
    phone = models.IntegerField(null=True,blank=True)
    quantity=models.IntegerField(null=True,blank=True)

    def __str__(self):
        return  f"{self.name}"


