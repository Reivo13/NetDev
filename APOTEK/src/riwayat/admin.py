from django.contrib import admin
from .models import Pembelian, Invoice, ItemInvoice

admin.site.register(Pembelian)
admin.site.register(Invoice)
admin.site.register(ItemInvoice)
