from django.contrib import admin
from pizzainfo.models import Pizzas

# Register your models here.

class PizzasAdmin(admin.ModelAdmin):
	list = ['pizzatype','pizzasize','pizzatoppings']

admin.site.register(Pizzas,PizzasAdmin)

