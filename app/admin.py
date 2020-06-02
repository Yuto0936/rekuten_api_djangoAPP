from django.contrib import admin
from .models import SearchWord, CD


class SearchWordAdmin(admin.ModelAdmin):
    list_display = ('pk', 'word')


class CDAdmin(admin.ModelAdmin):
    list_display = ('pk', 'word', 'jan', 'salesDate', 'title', 'itemPrice', 'imageUrl', 'reviewAverage', 'reviewCount')


admin.site.register(SearchWord, SearchWordAdmin)
admin.site.register(CD, CDAdmin)
