from django import forms
from pizzainfo.models import Pizzas

class PizzaForm(forms.ModelForm):
	class Meta:
		model = Pizzas
		fields = '__all__'
		

