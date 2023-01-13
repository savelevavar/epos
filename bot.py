from aiogram.utils.exceptions import BotBlocked
import logging
from aiogram import Bot, Dispatcher, executor, types
from os import getenv
from sys import exit
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.utils.markdown import code


login = None
password = None

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
    await message.answer('Для ввода пароля используйте /login, введите в формате ' + code('/login ваш логин пользователя'))
    await message.answer('Для ввода пароля используйте /password, аналогично логину')
    await GetUserInfo.waiting_for_user_login.set()


@dp.errors_handler(exception=BotBlocked)
async def error_bot_blocked(update: types.Update, exception: BotBlocked):
    # Update: объект события от Telegram. Exception: объект исключения
    # Здесь можно как-то обработать блокировку, например, удалить пользователя из БД
    print(f"Меня заблокировал пользователь!\nСообщение: {update}\nОшибка: {exception}")

    # Такой хэндлер должен всегда возвращать True,
    # если дальнейшая обработка не требуется.
    return True

@dp.message_handler(commands = ['login'])
async def example_command(message: types.Message):
    global login
    login = message.text.split(maxsplit=1)[1]
    await message.answer(f'Логин {login} получен!')

@dp.message_handler(commands = ['password'])
async def example_command(message: types.Message):
    global password
    password = message.text.split(maxsplit=1)[1]
    await message.answer(f'Пароль {password} получен!')

if __name__ == "__main__":
    # Запуск бота
    executor.start_polling(dp, skip_updates=True)