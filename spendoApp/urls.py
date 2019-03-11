from django.urls import path

from . import views

app_name = 'spendoApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:categoryId>', views.category, name='category'),

    path('category/categoryAgregar', views.categoryAgregar, name='categoryAgregar'),
    path('category/categoryAgregarForm', views.categoryAgregarForm, name='categoryAgregarForm'),

    path('category/categoryUpdate/<int:id>', views.categoryUpdateForm, name='categoryUpdateForm'),
    path('category/update/<int:id>', views.categoryUpdate, name='categoryUpdate'),

    path('category/<int:categoryId>/delete', views.categoryDelete, name='categoryDelete'),
    path('categories', views.categoriesListar, name='categoriesListar'),

    path('contact_us', views.contact_us, name='contactUs'),



    path('register/<int:registerId>', views.register, name='register'),

    path('register/registerAgregar', views.registerAgregar, name='registerAgregar'),
    path('register/registerAgregarForm', views.registerAgregarForm, name='registerAgregarForm'),

    path('register/registerUpdate/<int:id>', views.registerUpdateForm, name='registerUpdateForm'),
    path('register/update/<int:id>', views.registerUpdate, name='registerUpdate'),

    path('register/<int:categoryId>/delete', views.registerDelete, name='registerDelete'),
    path('registers', views.registersListar, name='registersListar'),

    path('contact_us', views.contact_us, name='contactUs'),
]