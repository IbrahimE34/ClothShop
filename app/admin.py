from django.contrib import admin

from app.models import Shop, Cloth, Category, Shop_Cloth

admin.site.register(Shop)
admin.site.register(Cloth)
admin.site.register(Category)
admin.site.register(Shop_Cloth)

# Register your models here.
