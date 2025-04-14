from django.contrib import admin
from django.urls import path
from app import views
from app.views import shop_cloth_list, add_clothes_to_shop

urlpatterns = [
    path("shop/",views.ShopCreate.as_view()),
    path("list/shop/",views.ShopList.as_view()),
    path("update/",views.ShopUpdate.as_view()),
    path("destroy/",views.ShopDestroy.as_view()),
    path("retrieve/",views.ShopRetrieve.as_view()),
    path('list/', shop_cloth_list, name='shop_cloth_list'),
    path("add-clothes/", add_clothes_to_shop, name="add_clothes_to_shop")
]