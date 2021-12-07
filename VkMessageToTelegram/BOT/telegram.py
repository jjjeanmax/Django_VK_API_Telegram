import logging
import requests
from aiogram import Bot, Dispatcher, types

from secret import get_secret
from data_fetch import get_last_sms


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=get_secret(section='TELEGRAM', setting='TELEGRAM_TOKEN'))
dp = Dispatcher(bot,loop=True,run_tasks_by_default=True)



@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when client send `/start` or `/help` commands.
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by jjjmax.")


@dp.message_handler(commands=['message'])
async def echo(message: types.Message):
    # get last message
    res = await get_last_sms()
    await bot.send_message(message.chat.id, f"message from {res['first_name']} {res['last_name']}")
    await bot.send_message(message.chat.id, f"message: {res['message']}")
