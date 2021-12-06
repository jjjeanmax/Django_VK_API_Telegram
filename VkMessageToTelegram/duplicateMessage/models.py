from django.db import models


class UserGroup(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    message = models.JSONField(verbose_name='содержимое сообщения (JSON)', null=True, blank=True)
    send_message = models.BooleanField(default=True)
    create_at = models.IntegerField(unique=True)

    def __str__(self):
        return f"{self.message} from user {self.first_name} {self.last_name} "

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'Groups User'
