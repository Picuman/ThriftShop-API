from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # If we had a base include like this, keep it, otherwise comment it out:
    # path('', include('your_app_name.urls')), 
]    