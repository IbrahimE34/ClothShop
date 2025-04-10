from django.shortcuts import render
from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.pagination import PageNumberPagination

from app.models import Shop
from app.serializers import ShopSerializers


# Create your views here.


class ShopCreate(CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializers

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

