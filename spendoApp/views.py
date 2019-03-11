from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from . models import Categories, Register

def index(request):
	return render(request, 'spendoApp/home.html')

def home(request):
	return HttpResponse('Página de inicio')

def contact_us(request):
	return render(request, 'spendoApp/contactUs.html')	


# ---------------Categories-----------------------

def category(request, categoryId):
	category = Categories.objects.get(pk = categoryId)
	return render(request, 'spendoApp/category.html', { 'category': category })

def categoriesListar(request):
	cats = Categories.objects.order_by('nombre')
	context = { 'categories': cats }
	return render(request, 'spendoApp/categories.html' , context)




def categoryUpdateForm(request, id):
	q = Categories.objects.get(pk = id)
	context = { 'category': q }
	return render(request, 'spendoApp/categoryEditar.html', context)

def categoryUpdate(request, id):
	try: 
		q = Categories.objects.get(pk = id)

		q.nombre = request.POST['name']
		q.medida = request.POST['medida']
		q.save()
		return HttpResponseRedirect(reverse('spendoApp:categoriesListar'))
	except Exception as e:
		return HttpResponse("Hubo un error intentando editar el programa" %e)




def categoryDelete(request, categoryId):
	try:
		category = Categories.objects.get(pk = categoryId)
		category.delete()
		messages.add_message(request, messages.SUCCESS, "The category has been deleted!")
		return HttpResponseRedirect('/spendoApp/categories')
	
	except Exception as e:
		return HttpResponse("Hubo un error intentando eliminar: <br>%s"%e)




def categoryAgregarForm(request):
	return render(request, 'spendoApp/categoryAgregar.html')

def categoryAgregar(request):
	try:
		q = Categories(
			medida = request.POST['medida'],
			nombre = request.POST['name']
		)
		q.save()
		
		messages.add_message(request, messages.SUCCESS, "The category has been created!")
		return HttpResponseRedirect(reverse('spendoApp:categoriesListar'))
	except Exception as e:
		return HttpResponse("Hubo un error intentando guardar el programa")


#------------------------Registers-------------------------------

def register(request, categoryId):
	register = Register.objects.get(pk = categoryId)
	return render(request, 'spendoApp/register.html', { 'register': register })

def registersListar(request):
	registers = Register.objects.order_by('nombre')
	context = { 'categories': cats }
	return render(request, 'spendoApp/categories.html' , context)




def registerUpdateForm(request, id):
	q = Register.objects.get(pk = id)
	context = { 'register': q }
	return render(request, 'spendoApp/registerEditar.html', context)

def registerUpdate(request, id):
	try: 
		q = Register.objects.get(pk = id)

		q.nombre = request.POST['name']
		q.medida = request.POST['medida']
		q.save()
		return HttpResponseRedirect(reverse('spendoApp:registerListar'))
	except Exception as e:
		return HttpResponse("Hubo un error intentando editar el programa" %e)




def registerDelete(request, registerId):
	try:
		register = Register.objects.get(pk = registerId)
		register.delete()
		messages.add_message(request, messages.SUCCESS, "The register has been deleted!")
		return HttpResponseRedirect('/spendoApp/registers')
	
	except Exception as e:
		return HttpResponse("Hubo un error intentando eliminar: <br>%s"%e)




def registerAgregarForm(request):
	return render(request, 'spendoApp/registerAgregar.html')

def registerAgregar(request):
	try:
		q = Register(
			medida = request.POST['medida'],
			nombre = request.POST['name']
		)
		q.save()
		
		messages.add_message(request, messages.SUCCESS, "The register has been created!")
		return HttpResponseRedirect(reverse('spendoApp:registerListar'))
	except Exception as e:
		return HttpResponse("Hubo un error intentando guardar el programa")

	

