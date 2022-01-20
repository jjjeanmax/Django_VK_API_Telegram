from VkMessageToTelegram.vk import vkSession
from .models import UserGroup


def get_data():
    message = vkSession.method("messages.getConversations", {"peer_ids": 2000000026})

    id_chat = []
    for i in range(len(message['items'])):
        ids = message['items'][i]['conversation']['peer']['id']
        id_chat.append(ids)

    # TODO: 200000026 = 20000000 + id_chat  --> in variable
    if 2000000026 in id_chat:
        indx = id_chat.index(2000000026)
        id_user = message['items'][indx].get('last_message').get('from_id')
        mess = message['items'][indx].get('last_message').get('text')
        _date = message['items'][indx].get('last_message').get('date')

        user_inf = vkSession.method("users.get", {"user_id": id_user})

        # Save to database
        UserGroup.objects.update_or_create(
            first_name=user_inf[0]['first_name'],
            last_name=user_inf[0]['last_name'],
            message=mess,
            create_at=_date
        )
