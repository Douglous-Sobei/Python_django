from django.contrib import admin
from . models import My_books, Author, Address, Country

# Register your models here.

class My_booksAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("author", "rating",)
    list_display = ("title", "author",)

admin.site.register(My_books, My_booksAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)