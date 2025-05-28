from django.contrib import admin
from django.urls import path, include  # Import 'include'
from django.conf import settings
from django.conf.urls.static import static  # Import for media files

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('kitchen.urls')),  # Include all URLs from 'kitchen' app
]

# Serve media files (uploaded images) during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
