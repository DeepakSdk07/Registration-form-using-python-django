from django.contrib import admin
from .models import Datas

class DatasAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'address', 'contact', 'mail')
    search_fields = ('name', 'mail')

admin.site.register(Datas, DatasAdmin)
