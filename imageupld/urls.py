
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delete_image/<int:image_id>/', views.delete_image, name='delete_image'),
    path("", views.index, name='index'), # Specify a name for the index URL pattern
      path('update_image/<int:image_id>/', views.update_image, name='update_image'),  
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
