from django.contrib import admin
from prettyjson import PrettyJSONWidget
from django import forms

from .models import GroupVK, UserGroup


class JsonForm(forms.ModelForm):
    class Meta:
        model = UserGroup
        fields = '__all__'
        widgets = {
          'message_json': PrettyJSONWidget(),
        }


@admin.register(GroupVK)
class AdminGroupVk(admin.ModelAdmin):
    list_display = ['group_id', 'name']
    fields = ('group_id', 'name',)


@admin.register(UserGroup)
class AdminUserGroup(admin.ModelAdmin):
    form = JsonForm
    list_display = ('first_name', 'last_name', 'message', 'send_message', 'group_user',)
    fields = ('first_name', 'last_name', 'message', 'send_message', 'group_user',)

    def has_delete_permission(self, request, obj=None):
        return False

    # Пакет prettyjson не может работать с полем message_json при запрете на операцию редактирования
    # def has_change_permission(self, request, obj=None):
    #     return False

    def has_add_permission(self, request):
        return True
