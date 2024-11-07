from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
 
# Custom 404 error view
handler404 = 'home.views.error_404' 
# Custom 500 error view
handler500 = 'home.views.error_500' 


urlpatterns = [
    path('secret-panel/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('home.urls')),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)