from django.conf import settings
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from VkMessageToTelegram.vk import vkSession
from duplicateMessage.serializers import UserGroupSerialiser
from .models import UserGroup


class GetNewUserData(APIView):
    @staticmethod
    def get(request):
        qs = UserGroup.objects.values('first_name', 'last_name', 'message', 'create_at').order_by('-create_at').first()
        data = {
            'first_name': qs['first_name'],
            'last_name': qs['last_name'],
            'message': qs['message'],
            'create_at': int(qs['create_at']),
        }

        serializer = UserGroupSerialiser(data=data)
        # Проверка соответствия формата данных
        serializer.is_valid(raise_exception=True)

        return Response(data)


class PutNewUserMessageInChatData(APIView):
    @staticmethod
    def put(request):
        message = vkSession.method("messages.getConversations", {"peer_ids": 2000000026})

        id_chat = []
        for i in range(len(message['items'])):
            ids = message['items'][i]['conversation']['peer']['id']
            id_chat.append(ids)
        if 2000000026 in id_chat:
            indx = id_chat.index(2000000026)
            print(message['items'][indx].get('last_message'))
            id_user = message['items'][indx].get('last_message').get('from_id')
            mess = message['items'][indx].get('last_message').get('text')
            _date = message['items'][indx].get('last_message').get('date')

        data = {}
        user_inf = vkSession.method("users.get", {"user_id": id_user})
        data['first_name'] = user_inf[0]['first_name']
        data['last_name'] = user_inf[0]['last_name']
        data['message'] = mess
        data['create_at'] = _date

        serializer = UserGroupSerialiser(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data_to_save = UserGroup(
            first_name=user_inf[0]['first_name'],
            last_name=user_inf[0]['last_name'],
            message=mess,
            create_at=_date
        )
        qs = UserGroup.objects.values('first_name', 'last_name', 'message', 'create_at')
        for cr in qs:
            if cr['create_at'] == data['create_at']:
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)
        data_to_save.save()
        return Response(status=status.HTTP_201_CREATED, data="save")


# @method_decorator(csrf_exempt, name='dispatch')
# class VkHookView(View):
#     @staticmethod
#     def get(request):
#         d = json.loads(request.body.decode('utf-8'))
#
#         if d['secret'] == settings.VK_HOOK_SECRET and d['group_id'] == int(settings.VK_GROUP_ID):
#             if d['type'] == 'message_new':
#                 obj = d['object']
#                 message = obj['message']
#
#                 # Write Your code here
#
#             elif d['type'] == 'confirmation':
#                 return HttpResponse(settings.VK_CONFIRMATION_CODE)
#
#         return HttpResponse('ok')

#
# class GetInfoUser(APIView):
#     @staticmethod
#     def get(request, user_id):
#         user_inf = vkSession.method("users.get", {"user_id": user_id})
#         first_name = user_inf[0]['first_name']
#         last_name = user_inf[0]['last_name']
#
#         try:
#             groups_user = vkSession.method("groups.get", {"user_id": user_id})
#             # print(groups_user)
#             # message = vkSession.method("messages.search", {"group_id": 1})
#             # print(message)
#             group = [gr for gr in groups_user['items']]
#             name = []
#             for group_id in group:
#                 groups = vkSession.method("groups.getById", {"group_id": group_id})
#                 name.append(groups[0]['name'])
#             data = {
#                 "first_name": first_name,
#                 "last_name": last_name,
#                 # "message": message,
#                 "groups_user": name
#             }
#
#             serializer = UserGroupSerialiser(data=data)
#
#             # Проверка соответствия формата данных
#             serializer.is_valid(raise_exception=True)
#
#             return Response(data)
#
#         except Exception as e:
#             return HttpResponse(f'{first_name} {last_name} is {e}')
