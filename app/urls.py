from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path("shop/",views.ShopCreate.as_view()),
    path("list/",views.ShopList.as_view()),
    path("update/",views.ShopUpdate.as_view()),
    path("destroy/",views.ShopDestroy.as_view()),
    path("retrieve/",views.ShopRetrieve.as_view()),
]