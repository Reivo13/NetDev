from django.contrib import admin
from .models import Obat

@admin.register(Obat)
class ObatAdmin(admin.ModelAdmin):
    list_display = ('nama', 'kategori', 'stok', 'harga')
