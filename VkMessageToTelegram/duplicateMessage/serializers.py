from rest_framework import serializers

from .models import UserGroup


class UserGroupSerialiser(serializers.Serializer):
    first_name = serializers.CharField(max_length=255)
    last_name = serializers.CharField(max_length=255)
    message = serializers.JSONField()
    send_message = serializers.BooleanField(default=True)
    create_at = serializers.IntegerField()

    class Meta:
        model = UserGroup
