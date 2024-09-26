from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),     # URL for the admin panel
    path('', include('services.urls')),  # This points the root URL ('/') to the services app
]
