from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('', include('pages.urls')),
    path('articles/', include('articles.urls')),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
