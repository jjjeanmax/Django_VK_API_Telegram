from django.urls import path

from .views import GetNewUserData, PutNewUserMessageInChatData

urlpatterns = [
    # path('hook_view/', VkHookView.as_view(), name='my-view'),
    # path('userinfo/<user_id>', GetInfoUser.as_view(), name='info-user'),
    path('user/', GetNewUserData.as_view(), name='user'),
    path('newuser/', PutNewUserMessageInChatData.as_view(), name='new-user'),

]
