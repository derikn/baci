from django.contrib import admin
from assetdb.models import Asset, Ticket, Computer

class TicketInline(admin.TabularInline):
    model = Ticket
    extra = 0

class AssetAdmin(admin.ModelAdmin):
    inlines = [TicketInline]

class ComputerAdmin(admin.ModelAdmin):
	model = Computer
admin.site.register(Asset, AssetAdmin)
admin.site.register(Computer, ComputerAdmin)