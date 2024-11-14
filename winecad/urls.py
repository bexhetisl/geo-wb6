from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    #path('winecadapp', include('winecadapp.urls')),
    path('', admin.site.urls), 
]
#path('', admin.site.urls),  # Admin interface
 