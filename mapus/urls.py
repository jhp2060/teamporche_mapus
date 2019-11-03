from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('building_map/', include('building_map.urls', namespace='building_map')),
    path('campus_map/', include('campus_map.urls', namespace='campus_map')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
