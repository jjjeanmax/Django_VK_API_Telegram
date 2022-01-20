from django.urls import path

from .views import GetNewUserData, PutNewUserMessageInChatData

urlpatterns = [
    path('user/', GetNewUserData.as_view(), name='user'),
    path('newuser/<pk>', PutNewUserMessageInChatData.as_view(), name='new-user'),

]
