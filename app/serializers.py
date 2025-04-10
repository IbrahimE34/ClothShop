from rest_framework import serializers

from app.models import Shop, Category, Cloth


class ShopSerializers(serializers.ModelSerializer):


    class Meta:
        model = Shop
        fields = "__all__"

class CategorySerializers(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ["id", "name"]

class ClothSerializers(serializers.ModelSerializer):


    class Meta:
        model = Cloth
        fields = "__all__"


