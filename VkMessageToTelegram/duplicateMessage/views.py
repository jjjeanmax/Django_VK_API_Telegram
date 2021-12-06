from django.conf import settings
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json

from rest_framework.views import APIView
from rest_framework.response import Response

from VkMessageToTelegram.vk import vkSession
from duplicateMessage.serializers import UserGroupSerialiser


@method_decorator(csrf_exempt, name='dispatch')
class VkHookView(View):
    @staticmethod
    def get(request):
        d = json.loads(request.body.decode('utf-8'))

        if d['secret'] == settings.VK_HOOK_SECRET and d['group_id'] == int(settings.VK_GROUP_ID):
            if d['type'] == 'message_new':
                obj = d['object']
                message = obj['message']

                # Write Your code here

            elif d['type'] == 'confirmation':
                return HttpResponse(settings.VK_CONFIRMATION_CODE)

        return HttpResponse('ok')


class GetInfoUser(APIView):
    @staticmethod
    def get(request, user_id):

        user_inf = vkSession.method("users.get", {"user_id": user_id})
        first_name = user_inf[0]['first_name']
        last_name = user_inf[0]['last_name']

        try:
            groups_user = vkSession.method("groups.get", {"user_id": user_id})
            # print(groups_user)
            # message = vkSession.method("messages.search", {"group_id": 1})
            # print(message)
            group = [gr for gr in groups_user['items']]
            name = []
            for group_id in group:
                groups = vkSession.method("groups.getById", {"group_id": group_id})
                name.append(groups[0]['name'])
            data = {
                "first_name": first_name,
                "last_name": last_name,
                # "message": message,
                "groups_user": name
            }

            serializer = UserGroupSerialiser(data=data)

            # Проверка соответствия формата данных
            serializer.is_valid(raise_exception=True)

            return Response(data)

        except Exception as e:
            return HttpResponse(f'{first_name} {last_name} is {e}')


class GetUserData(APIView):
    @staticmethod
    def get(request, user_id):

        user_inf = vkSession.method("users.get", {"user_id": user_id})
        first_name = user_inf[0]['first_name']
        last_name = user_inf[0]['last_name']
        print(settings.VK_GROUP_ID)
        groups = vkSession.method("groups.getById", {"group_id": settings.VK_GROUP_ID})
        group_name = groups[0]['name']
        message = vkSession.method("messages.getConversations", {"user_id": user_id})
        print(message)

        data = {
            "first_name": first_name,
            "last_name": last_name,
            # "message": message,
            "groups_user": group_name
        }

        serializer = UserGroupSerialiser(data=data)

        # Проверка соответствия формата данных
        serializer.is_valid(raise_exception=True)

        return Response(data)
