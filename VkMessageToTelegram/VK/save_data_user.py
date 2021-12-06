import psycopg2

from typing import Union

from querries import query_insert_client_data, query_get_client_profile_by_name
from vk import vkSession


async def client_profile_get_or_create(pg_pool: object, first_name: str, last_name: str, send_message, message: str,
                                       date: str) -> Union[str, None]:
    """Взять или создать профиль клиента

    Parameters
    ----------
    pg_pool : object
        подключение к БД
    phone_number : str
        номер телефона

    Returns
    -------
    str
        uuid профиля клиента
    or None
    """

    async with pg_pool.acquire() as conn:
        async with conn.cursor() as cur:
            # Асинхронный запрос: взять uuid профиля клиента
            await cur.execute(query_get_client_profile_by_name(first_name, last_name))
            row = await cur.fetchone()
            client_profile_first_name = row[0] if row else None
            message = vkSession.method("messages.getConversations", {"peer_ids": 2000000026})

            id_chat = []
            for i in range(len(message['items'])):
                ids = message['items'][i]['conversation']['peer']['id']
                id_chat.append(ids)
            if 2000000026 in id_chat:
                indx = id_chat.index(2000000026)
                print(message['items'][indx].get('last_message'))
                id_user = message['items'][indx].get('last_message').get('from_id')
                mess = message['items'][indx].get('last_message').get('text')
                _date = message['items'][indx].get('last_message').get('date')

            # data = {}
            user_inf = vkSession.method("users.get", {"user_id": id_user})
            first_name = user_inf[0]['first_name']
            last_name = user_inf[0]['last_name']
            message = mess
            date = _date

            # Проверка наличия профиля клиента
            if client_profile_first_name is None:
                # Создание профиля клиента
                await cur.execute(
                    query_insert_client_data(
                        first_name,
                        last_name,
                        send_message,
                        message,
                        date
                    )
                )
