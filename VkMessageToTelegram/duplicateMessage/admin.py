from django.contrib import admin
from prettyjson import PrettyJSONWidget
from django import forms

from .models import UserGroup


class JsonForm(forms.ModelForm):
    class Meta:
        model = UserGroup
        fields = '__all__'
        widgets = {
          'message_json': PrettyJSONWidget(),
        }


@admin.register(UserGroup)
class AdminUserGroup(admin.ModelAdmin):
    form = JsonForm
    list_display = ('first_name', 'last_name', 'message', 'send_message','create_at',)
    fields = ('first_name', 'last_name', 'message', 'send_message',)

    def has_delete_permission(self, request, obj=None):
        return True

    # Пакет prettyjson не может работать с полем message_json при запрете на операцию редактирования
    # def has_change_permission(self, request, obj=None):
    #     return False

    def has_add_permission(self, request):
        return True
