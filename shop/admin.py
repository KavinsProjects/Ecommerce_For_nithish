from django.contrib import admin
from shop.models import produts


# Register your models here.


@admin.register(produts)
class produtsadmins(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'description', 'image']