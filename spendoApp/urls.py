from django.urls import path

from . import views

app_name = 'spendoApp'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:categoryId>', views.category, name='category'),
    path('category/categoryAgregar', views.categoryAgregar, name='categoryAgregar'),
    path('category/categoryAgregarForm', views.categoryAgregarForm, name='categoryAgregarForm'),
    path('category/<int:categoryId>/delete', views.categoryDelete, name='categoryDelete'),
    path('categories', views.categoriesListar, name='categoriesListar')
]