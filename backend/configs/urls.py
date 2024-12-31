from django.urls import include, path

urlpatterns = [
    path('auto', include('apps.categories.urls')),
    path('auto', include('apps.body_styles.urls')),
    path('auto', include('apps.adverts.urls')),
    path('auth', include('apps.auth.urls')),
    path('users', include('apps.user.urls')),
]
