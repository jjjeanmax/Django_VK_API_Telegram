from django.conf import settings
from vk_api import VkApi
from vk_api import VkUpload


# FIXME: Использовать Callback API-VK
#  Callback API — это инструмент для отслеживания активности пользователей в сообществе ВКонтакте.


vkSession = VkApi(token=settings.VK_ACCESS_TOKEN)
vk = vkSession.get_api()
vk_upload = VkUpload(vk)
