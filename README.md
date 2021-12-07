# Django_VK_API_Telegram
сервис Django который будет работать через API - VK и дублировать сообщения группы в VK в групповой чат в Telegram


Django REST - API, с методами:
-
    Получаем сообщение внутри группы VK
    Сохраняем в базу данных Postgres
    При получении сообщения от Нового пользователя в VK,  
    оправить сообщения “Пишет новый пользователь {Имя, Фамилия}”
    Отправляем сообщение в группу в Telegram

- USE CallBak vk-api to track user activity


## Старт

1. Создать и активировать виртуальное окружение:

    `python -m venv venv`

2. Установить пакеты :

    `pip install -r requirements.txt`

3. Выполнить команду для выполнения миграций:

    `python manage.py migrate`

4. Создать статичные файлы: 

    `python manage.py collectstatic`

5. Создать суперпользователя:

    `python manage.py createsuperuser`

6. Создать конфиг-файл:

    `configs.json`

7. Запустить сервер django:
    
    `$ python manage.py runserver`

8. Запустить сервер telegram из репозитории BOT :
    
    `$ python main.py`

### Документация доступна в docs:
> http://127.0.0.1:8000/docs/

