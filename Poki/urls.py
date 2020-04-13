from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("PokiBase.urls")),
    path('test/', include("Test.urls")),
    path('forum/', include("Forum.urls")),
    path('account/', include('django.contrib.auth.urls')),
    path('account/', include('account.urls')),
]
