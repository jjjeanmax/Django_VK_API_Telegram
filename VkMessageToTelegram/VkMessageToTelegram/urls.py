from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from duplicateMessage import urls as vk_urls
from .yasg import schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vk/', include(vk_urls)),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')

]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
