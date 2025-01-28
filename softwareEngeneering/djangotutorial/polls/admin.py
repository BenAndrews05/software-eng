from django.contrib import admin

from .models import Amount_Type, Item_Type, Individual_Items, Shopping_List 

admin.site.register(Amount_Type)
admin.site.register(Item_Type)
admin.site.register(Individual_Items)
admin.site.register(Shopping_List)