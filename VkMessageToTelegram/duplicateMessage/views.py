from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserGroupSerialiser
from .models import UserGroup
from .get_last_message_is_vk import get_data


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
            дата отправки сообщения
        Returns
        -------
        str
        """

    @staticmethod
    def get(request):
        get_data()
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


# For me
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
            дата отправки сообщения
        Returns
        -------
        str
        """

    @staticmethod
    def put(request, pk, format=None):
        qs = UserGroup.objects.get(id=pk)
        serializer = UserGroupSerialiser(qs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
