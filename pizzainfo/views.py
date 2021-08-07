from django.shortcuts import render,redirect
from pizzainfo.models import Pizzas
from pizzainfo.forms import PizzaForm


# Create your views here.

def retrieve_view(request):
	pizza = Pizzas.objects.all()
	return render(request,'pizzainfo/index.html',{'pizza':pizza})


def create_view(request):
	form = PizzaForm()
	if request.method == 'POST':
	   	form = PizzaForm(request.POST)
	   	if form.is_valid():
	      		form.save()

	return render(request,'pizzainfo/create.htm',{'form':form})


def delete_view(request,id):
    pizza = Pizzas.objects.get(id)
    if request.method == 'POST':
    pizza.delete()












'''
def create_view(request):
	form = PizzaForm()
	if request.method == 'POST':
	   	form = PizzaForm(request.POST)
	   	if form.is_valid():
	      		form.save()

	return render(request,'pizzainfo/create.htm',{'form':form})


def delete_view(request,id=None):
    pizza = Pizzas.objects.get(id=None)
    pizza.delete()

'''







