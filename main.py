from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN
from lists import *
import random

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['test'])
async def process_start_command(message: types.Message):
    await message.reply(".")


@dp.message_handler(content_types=types.ContentType.VOICE)
async def process_help_command(message: types.Message):
    print("Bot request:")
    print("    User:", message.from_user.first_name)
    print("    Chat:", message.chat.first_name)

    await message.reply(random.choice(VOICE_REPLIES))


if __name__ == '__main__':
    executor.start_polling(dp)
