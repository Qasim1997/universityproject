from django.contrib import admin

# Register your models here.
from home.models import City, Hotel, Cart, UserDetail, Book


class UserDetailAdmin(admin.ModelAdmin):
    list_display =  ('first_name', 'last_name','email', 'phone_number', 'date_reserve','notes')


class HotelAdmin(admin.ModelAdmin):
    list_display = ('title', 'city','price')

class BookAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel','quantity')

admin.site.register(Cart)
admin.site.register(City)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(Book, BookAdmin )
admin.site.register(UserDetail, UserDetailAdmin)


