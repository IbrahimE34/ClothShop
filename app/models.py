from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=15, verbose_name="Mini name")
    full_name = models.CharField(max_length=20, verbose_name="Full name")

    def __str__(self):
        return f"{self.name} - {self.full_name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Cloth(models.Model):
    name = models.CharField(max_length=15)
    brand = models.CharField(max_length=25)
    price = models.IntegerField()
    country_of_origin = models.CharField(max_length=50)
    added_at = models.DateTimeField()
    size = models.IntegerField()
    category = models.ForeignKey(Category, related_name="clothes", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.brand}, {self.country_of_origin})"


class Shop(models.Model):
    address = models.CharField(max_length=30)
    name = models.CharField(max_length=15)
    created_at = models.DateTimeField()
    # clothes = models.ManyToManyField(Cloth, through="ShopCloth", related_name="shops")

    def __str__(self):
        return f"Магазин: {self.name}, адрес: {self.address}"

    def total_cloth_quantity(self):
        return self.shop_clothes.aggregate(total=models.Sum("quantity"))["total"] or 0

    def add_clothes(self, cloth_quantities):
        for item in cloth_quantities:
            cloth = item.get('cloth')
            quantity = item.get("quantity", 1)
            shop_cloth, created = ShopCloth.objects.get_or_create(
                shop=self,
                cloth=cloth
            )
            shop_cloth.quantity += quantity if not created else 0
            shop_cloth.save()


class ShopCloth(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name="shop_clothes")
    cloth = models.ForeignKey(Cloth, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.shop} x {self.cloth} — {self.quantity} шт."






