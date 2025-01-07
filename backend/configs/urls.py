from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('auto', include('apps.categories.urls')),
    path('auto', include('apps.car_model.urls')),
    path('auto', include('apps.adverts.urls')),
    path('auth', include('apps.auth.urls')),
    path('users', include('apps.user.urls')),
    path('auto', include('apps.auto_salon.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
