# Register your models here.


from django.contrib import admin
from .forms import StockCreateForm
from .models import Stock
from .models import Categorie
from .models import StockListHistory



# admin_customization
# make display tables in admin

class StockCreateAdmin(admin.ModelAdmin):

    list_display = ['category','item_name','quantity']  # for maing tables in admin view
    form = StockCreateForm
    list_filter = ['category']   #for filters
    search_fields = ['category','item_name']  #for search


# admin.site.register(StockCreateAdmin)
admin.site.register(Stock, StockCreateAdmin)
admin.site.register(Categorie)
admin.site.register(StockListHistory)


# import forms