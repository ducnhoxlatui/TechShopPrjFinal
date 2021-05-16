from django.contrib import admin
from.models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pro_name','group','pro_price')  #lựa chọn phương thức hiển thị trên trang admin
    search_fields = ('pro_name', )


class OrderAdmin(admin.ModelAdmin):
    list_display = ('totmoney',)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('cus_id','name')
    search_fields = ('name',)


admin.site.register(Product,ProductAdmin)  # đăng kí class lên trên trang admin để dễ quản lý
admin.site.register(PGroup)
admin.site.register(Brand)
admin.site.register(Order,OrderAdmin)
admin.site.register(Customer,CustomerAdmin)
admin.site.register(OderDetail)






