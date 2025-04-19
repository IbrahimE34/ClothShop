from http.client import HTTPResponse
from venv import create

from django.core.serializers import serialize
from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.templatetags.rest_framework import items

from app.models import Shop, Cloth
from app.serializers import ShopSerializers, AddClothesToShopSerializers

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ShopCloth
from .serializers import ShopClothSerializer
# Create your views here.


class ShopCreate(CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers
    def perform_create(self, serializer):
        name = serialize.validated_data["name"]
        address = serialize.validated_data["address"]
        shop, created = Shop.objects.get_or_create(
            name=name, address=address,
            defaults ={"create_at": serializer.valedated_data.get("created_at")}
        )
        self.shop= shop



class ShopApiListPagination(PageNumberPagination):
    page_size = 2
    page_query_param = "page_size"
    max_page_size = 3

class ShopList(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers
    pagination_class = ShopApiListPagination

class ShopRetrieve(RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers


class ShopUpdate(UpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers


class ShopDestroy(DestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers

@api_view(['GET'])
def shop_cloth_list(request):
    shop_clothes = ShopCloth.objects.select_related('shop', 'cloth').all()
    serializer = ShopClothSerializer(shop_clothes, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def add_clothes_to_shop(request):
    serializer = AddClothesToShopSerializers(data=request.data)
    if serializer.is_valid():
        shop_id = serializer.validated_data["shop_id"]
        clothes_data  = serializer.validated_data["clothes"]

        try:
            shop = Shop.objects.get(id=shop_id)
        except Shop.DoesNotExist:
            return Response({"error": "Магазин не найден"}, status=status.HTTP_404_NOT_FOUND)

        for item in clothes_data:
            cloth_id =item["cloth_id"]
            quantity = item["quantity"]
            try:
                cloth = Cloth.objects.get(id= cloth_id)
            except Cloth.DoesNotExist:
                return Response({"error": f"Одежда с id={cloth_id}не найдена"},status=status.HTTP_404_NOT_FOUND)

            shop_cloth, created = ShopCloth.objects.get_or_create(shop=shop, cloth=cloth)
            if created:
                shop_cloth.quantity = quantity
            else:
                shop_cloth.quantity += quantity
                shop_cloth.save()
        return Response({"success": "Одежда добавлена"}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
