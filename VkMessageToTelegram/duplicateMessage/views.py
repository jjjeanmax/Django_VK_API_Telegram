from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from get_last_message_is_vk import get_data
from duplicateMessage.serializers import UserGroupSerialiser
from .models import UserGroup


class GetNewUserData(APIView):
    """ получение сообщения от Нового пользователя в VK

        Parameters
        ----------
        first_name : str
            Имя

        last_name : str
            Фамилия

        message : str
            Сообщение

        create_at : int
            дата отправки сообщение
        Returns
        -------
        str
        """

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
    """ обновление сообщения пользователя в VK

        Parameters
        ----------
        first_name : str
            Имя

        last_name : str
            Фамилия

        message : str
            Сообщение

        create_at : int
            дата отправки сообщение
        Returns
        -------
        str
        """
    @staticmethod
    def put(request):
        data = get_data()
        print(data)

        serializer = UserGroupSerialiser(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data_to_save = UserGroup(
            first_name=data['first_name'],
            last_name=data['last_name'],
            message=data['message'],
            create_at=data['create_at']
        )

        qs = UserGroup.objects.values('first_name', 'last_name', 'message', 'create_at')
        for cr in qs:
            if cr['create_at'] == data['create_at']:
                return Response(serializer.errors, status=status.HTTP_409_CONFLICT)

        # TODO: celery task
        data_to_save.save()
        return Response(status=status.HTTP_201_CREATED, data="save")
