import logging
from aiogram import Bot, Dispatcher, executor, types


bot = Bot(token="5154655086:AAEJatzVb9H163lz6pabcN7k3N7P6TdnuOU")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


# Хэндлер на команду /start
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Ученик", callback_data="type_of_student"))
    await message.answer('''Добро пожаловать в бота \"Эпос\".
Авторизуйтесь для дальнейшей работы, для этого выберите тип пользователя''', reply_markup=keyboard)


@dp.callback_query_handler(text="type_of_student")
async def send_random_value(call: types.CallbackQuery, message: types.Message):
    await call.message.answer('Тип пользователя, ученик, установлен')
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Вход с паролем", callback_data="login_with_password"))
    await bot.send_message('''Выберите способ авторизации''', reply_markup=keyboard)


# @dp.callback_query_handler(text="login_with_password")
# async def send_random_value(call: types.CallbackQuery):
#     await call.message.answer('Выбран вход с паролем')
#     await message.answer('''Ответом на это сообщение введите логин пользователя''')

@dp.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
