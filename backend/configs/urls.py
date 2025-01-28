from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('api/auto', include('apps.adverts.urls')),
    path('api/auto', include('apps.categories.urls')),
    path('api/auto', include('apps.auto_salon.urls')),
    path('api/auto', include('apps.car_mark.urls')),
    path('api/auto', include('apps.car_model.urls')),

    path('api/auto', include('apps.currency.urls')),
    path('api/auth', include('apps.auth.urls')),
    path('api/users', include('apps.user.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
