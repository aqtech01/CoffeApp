from django.contrib import admin
from core.models import *

class CoffeAdmin(admin.ModelAdmin):
    list_display = ('name','price','stock')
# Register your models here.
admin.site.register(Coffe,CoffeAdmin)