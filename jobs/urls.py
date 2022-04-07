from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jobs.api')),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('user.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
