from symtable import Class

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15, verbose_name= "Mini name ")
    full_name = models.CharField(max_length=20, verbose_name= "Full name")

    def __str__(self):
        return f"{self.name}-{self.full_name}"


    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категорий"

class Shop(models.Model):
    address = models.CharField(max_length=30)
    name = models.CharField(max_length=15)
    data = models.DateTimeField()
    cloths = models.ManyToManyField(Category, related_name="cloths")


    def total_cloth_quantity(self):
        return self.shop_cloth_set.aggregate(total=models.Sum("quantity"))["total"]  or 0


class Cloth(models.Model):
    name = models.CharField(max_length=15)
    brand = models.CharField(max_length=25)
    prise = models.IntegerField()
    Create_Country = models.CharField(max_length=50)
    data = models.DateTimeField()
    size = models.IntegerField
    category = models.ForeignKey(Category, related_name="categories", on_delete=models.CASCADE)





class Shop_Cloth(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.shop} x {self.cloth} in {self.quantity}"

# class Shop_Sklad(models.Model):
#     for shop_cloth in shop.shopcloth_set.all():
#     shop = Shop.objects.get(name="My Shop")


