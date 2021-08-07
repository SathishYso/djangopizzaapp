from django.db import models

# Create your models here.

class Pizzas(models.Model):
	pizzatype = models.CharField(max_length=30)
	pizzasize = models.CharField(max_length=30)
	pizzatoppings = models.CharField(max_length=30)
	
	
