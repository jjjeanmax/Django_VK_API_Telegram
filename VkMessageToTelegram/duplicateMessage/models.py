from django.db import models


class GroupVK(models.Model):
    group_id = models.IntegerField(verbose_name='id Group', unique=True, blank=False)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = 'Group Vk'
        verbose_name_plural = 'Groups Vk'


class UserGroup(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    message = models.JSONField(verbose_name='содержимое сообщения (JSON)', null=True, blank=True)
    send_message = models.BooleanField(default=False)
    group_user = models.ForeignKey(GroupVK, on_delete=models.CASCADE, verbose_name='Group User')

    def __str__(self):
        return f"{self.message} from user {self.first_name} {self.last_name} is {self.group_user}"

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Groups User'
