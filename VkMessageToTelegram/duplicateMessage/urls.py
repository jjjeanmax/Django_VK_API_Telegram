from django.urls import path

from .views import GetInfoUser, VkHookView,GetUserData

urlpatterns = [
    path('hook_view/', VkHookView.as_view(), name='my-view'),
    path('userinfo/<user_id>', GetInfoUser.as_view(), name='info-user'),
    path('user/<user_id>', GetUserData.as_view(), name='user'),

]
