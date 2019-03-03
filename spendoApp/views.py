from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages


from . models import Categories

def index(request):
	return render(request, 'spendoApp/index.html')

def home(request):
	return HttpResponse('Página de inicio')

def category(request, categoryId):
	category = Categories.objects.get(pk = categoryId)
	return render(request, 'spendoApp/category.html', { 'category': category })

def categoriesListar(request):
	cats = Categories.objects.order_by('nombre')
	context = { 'categories': cats }
	return render(request, 'spendoApp/categories.html' , context)

def categoryDelete(request, categoryId):
	category = Categories.objects.get(pk = categoryId)
	category.delete()
	messages.add_message(request, messages.SUCCESS, "The category has been deleted!")
	return HttpResponseRedirect('/spendoApp/categories')

def categoryAgregarForm(request):
	return render(request, 'spendoApp/categoryAgregar.html')

def categoryAgregar(request):
	q = Categories(
		medida = request.POST['medida'],
		nombre = request.POST['name']
	)
	q.save()
	
	messages.add_message(request, messages.SUCCESS, "The category has been created!")
	return HttpResponseRedirect(reverse('spendoApp:categoriesListar'))

	

	

