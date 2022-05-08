# Django_VK_API_Telegram
Django service that will work through the API - VK and duplicate group messages in VK in a group chat in Telegram

Django REST - API, with methods:
-
     We receive a message inside the VK group
     Saving to a Postgres database
     When receiving a message from a New user in VK,
     send messages “Written by a new user {Name, Surname}”
     Sending a message to a group in Telegram

- USE CallBak vk-api to track user activity


## Start

1. Create and activate virtual environment:

    `python -m venv venv`

2. Install packages:

    `pip install -r requirements.txt`

3. Run migrations:

    `python manage.py migrate`

4. Create superuser:

    `python manage.py createsuperuser`

4. Create config file:

    `configs.json`

6. Start django server:
    
    `$ python manage.py runserver`

7. Start telegram server from BOT repository:
    
    `$ python main.py`

### Documentation is available in docs:
> http://127.0.0.1:8000/docs/

