from rest_framework import serializers

from app.models import Shop, Category, Cloth, ShopCloth


class ShopSerializers(serializers.ModelSerializer):


    class Meta:
        model = Shop
        fields = ['id', 'name', 'address']

    def validate(self,attrs):
        name = attrs.get("name")
        address = attrs.get("address")
        if Shop.objects.filter(name+name, address=address).exists():
            raise serializers.ValidationError("Магазин с таким названием и адресом уже есть")
        return attrs


class CategorySerializers(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ["id", "name"]

class ClothSerializers(serializers.ModelSerializer):


    class Meta:
        model = Cloth
        fields = ['id', 'name', 'brand', 'size']

class ShopClothSerializer(serializers.ModelSerializer):
    shop = ShopSerializers()
    cloth = ClothSerializers()

    class Meta:
        model = ShopCloth
        fields = ['shop', 'cloth', 'quantity']


class AddClothItemSerializer(serializers.Serializer):
    cloth_id = serializers.IntegerField()
    quantity = serializers.IntegerField(default=1, min_value=1)

class AddClothesToShopSerializers(serializers.Serializer):
    shop_id = serializers.IntegerField()
    clothes = AddClothItemSerializer(many=True)

