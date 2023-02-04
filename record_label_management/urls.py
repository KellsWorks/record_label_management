from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('', include('landing.urls')),
    path('admin/', admin.site.urls),
    # path(r'^schedule/', include('schedule.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
