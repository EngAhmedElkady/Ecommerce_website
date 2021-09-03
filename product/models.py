from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Product(models.Model):
    prod_name=models.CharField(max_length=200 ,verbose_name=_("product name "))
    prod_description=models.TextField(max_length=2000,verbose_name=_("product decription"))
    prod_price=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("product price"))
    prod_cost=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("product cost "))
    # image=models.ImageField()
    prod_created=models.DateTimeField(auto_now_add=True,verbose_name=_("product created"))

    def __str__(self):
        return self.prod_name



class ProductImage(models.Model):
    prodproduct=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_("product"))
    prodimage=models.ImageField(upload_to="product/",verbose_name=_("product_image"))

    class Meta:
        verbose_name=_("ProductImge")
        verbose_name_plural=_("ProductImge")
    def __str__(self):
        return str(self.prodproduct)+" "+"image"

class Category(models.Model):
    Catname=models.CharField(max_length=50,verbose_name=_("name"))
    Catparent=models.ForeignKey('self',limit_choices_to={"Catparent__isnull":True},on_delete=models.CASCADE ,null=True,blank=True)
    Catdesc=models.TextField(verbose_name=_(" category description"))
    Catimg=models.ImageField(upload_to="category/")


    class Meta:
        verbose_name=_("Category")
        verbose_name_plural=_("Categories")

    def __str__(self):
        return self.Catname


class ProductAlternative(models.Model):
    PALproduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="main_product")
    PALAlternative=models.ManyToManyField(Product ,related_name="Alternative_products")

    class Meta:
        verbose_name=_("ProductAlternative")
        verbose_name_plural=_("ProductAlternatives")

    def __str__(self):
        return str(self.PALproduct)


class ProductAccessores(models.Model):
    PAcproduct=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="mainAccessory_product")
    PAcAlternative=models.ManyToManyField(Product ,related_name="Accessory_products")

    class Meta:
        verbose_name=_("ProductAccessores")
        verbose_name_plural=_("ProductAccessores")

    def __str__(self):
        return str(self.PAcproduct)





    

     



# category
# image
# alternative
# accessories



