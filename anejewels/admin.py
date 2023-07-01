from django.contrib import admin
from .models import Category,Product,Order,OrderProduct,MyTransaction
# Register your models here.


admin.site.register(Category)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quantity', 'price')
    list_filter = ('category',)
    search_fields = ('name',)
    
   
    def has_view_permission(self, request, obj=None):
        return True

    # def has_delete_permission(self, request, obj=None):
    #     if obj and (request.user == obj.user) or request.user.is_superuser:
    #         return True
    #     return False
    
    # def has_change_permission(self, request, obj=None):
    #     if obj and (request.user == obj.user) or request.user.is_superuser:
    #         return True
    #     return False


admin.site.register(Product,ProductAdmin)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'description', 'total')
    
    def has_view_permission(self, request, obj=None):
        return True
admin.site.register(Order,OrderAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ('order', 'product')

admin.site.register(OrderProduct,OrderProductAdmin)



# admin.site.register(MyTransaction)