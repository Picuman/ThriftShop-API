from django.urls import path
from . import views

urlpatterns = [
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('items/', views.ItemList.as_view(), name='item-list'),
]