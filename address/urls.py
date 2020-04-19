from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('home/', views.home,name="home"),
    path('add/',views.add,name="add"),
    path('edit/<list_id>', views.edit, name="edit"),
    path('delete/<list_id>', views.delete, name="delete"),
]