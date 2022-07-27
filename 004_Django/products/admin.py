from django.contrib import admin
from .models import Product 

class ProductAdmin(admin.ModelAdmin):
    # pass
    list_display = [ 'name', 'price', 'content', 'category', 'active' ]
    # list_display = [ 'name', 'price' ]
    # 
    list_display_links = ['name', 'content']
    # To Determine What Fireld Can Be Edit Without open The Product 
    list_editable = ['price','category']
    
    # To Put Search Field  By Name Can Change To Other 
    search_fields = ['name']
    # To Filter Product
    list_filter   = ['category', 'price']
    # To Determine What showd be apper in 
    # fields = ['name', 'price', category]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.site_header = 'hamzoooz'
admin.site.site_title = 'Admin  || hamzoooz'
# admin.site.register(Test)




