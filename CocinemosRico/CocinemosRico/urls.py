from django.contrib import admin
from django.urls import path, include

from CocinemosRico.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),

    path('recipes/', include('recipes.urls')),
]
