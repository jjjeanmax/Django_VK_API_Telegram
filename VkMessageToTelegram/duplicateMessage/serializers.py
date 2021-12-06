from rest_framework import serializers

from .models import UserGroup


class UserGroupSerialiser(serializers.Serializer):
    class Meta:
        model = UserGroup
        fields = [
            'first_name',
            'last_name',
            'message',
            'send_message',
        ]
