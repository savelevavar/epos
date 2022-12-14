from aiogram.utils.exceptions import BotBlocked
import logging
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from sys import exit
from aiogram.dispatcher.filters.state import State, StatesGroup


bot_token = getenv("BOT_TOKEN")
if not bot_token:
    exit("Error: no token provided")

bot = Bot(token=bot_token)
# Диспетчер для бота
dp = Dispatcher(bot)
# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)

class GetUserInfo(StatesGroup):
    waiting_for_user_login = State()
    waiting_for_user_password = State()


@dp.message_handler(commands=['start'])
async def get_user_mailbox(message: types.Message):
    chat_id = message.chat.id
    await message.answer('Enter your login: ')
    await GetUserInfo.waiting_for_user_login.set()


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True

@dp.message_handler(commands="answer")
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message_handler(commands="reply")
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')

@dp.message_handler(commands="login")
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')


if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)