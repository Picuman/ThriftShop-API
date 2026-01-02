from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    # Auth Endpoints
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', obtain_auth_token, name='login'),

    # Category Endpoints
    path('categories/', views.CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetail.as_view(), name='category-detail'),
    
    # Item Endpoints
    path('items/', views.ItemList.as_view(), name='item-list'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
]