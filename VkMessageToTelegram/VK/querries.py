
def query_insert_client_data(first_name: str, last_name: str,send_message, message: str, date: str) -> str:
    """Создать клиента

    Parameters
    ----------
    phone_number : str
        номер телефона

    Returns
    -------
    str
        строка SQL запроса
    """

    return '''INSERT INTO duplicateMessage_usergroup 
    (last_name, first_name, send_message, message, created_at) 
    VALUES ('{0}', '{1}', TRUE, '{3}', '{4}')'''.format(
        last_name,
        first_name,
        send_message,
        message,
        date
    )


def query_get_client_profile_by_name(first_name: str, last_name:str) -> str:
    """Получить клиента по номеру телефона

    Parameters
    ----------
    phone_number : str
        номер телефона

    Returns
    -------
    str
        строка SQL запроса
    """

    return "SELECT id FROM duplicateMessage_usergroup WHERE first_name = '{0}, and last_name= {1}' LIMIT 1".format(first_name,last_name)