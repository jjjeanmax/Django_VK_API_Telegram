from django.contrib import admin
from django.urls import path,include
from duplicateMessage import urls as vk_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vk/', include(vk_urls)),
]
