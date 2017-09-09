from django.contrib import admin
from .models import Cake,CustomCake,OrderCake
from django.db.models.functions import Lower
# Register your models here.
class CakeAdmin(admin.ModelAdmin):

	list_display = ['name','price','cake_type','flavour','weight']
	list_display_links = ['name']
	list_editable = ['price']
	list_filter = ['timestamp']
	search_fields = ['name']
	ordering = ['name']
	def get_ordering(self, request):
		return [Lower('name')]
	class meta:
		model = Cake

admin.site.register(Cake,CakeAdmin)
admin.site.register(CustomCake)
admin.site.register(OrderCake)
