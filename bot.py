import telebot
import datetime
from telebot import types

bot = telebot.TeleBot('5154655086:AAEJatzVb9H163lz6pabcN7k3N7P6TdnuOU')


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Добро пожаловать в бота "Эпос". Авторизуйтесь для дальнейшей работы')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    student_type = types.KeyboardButton("Я ученик")
    markup.add(student_type)
    bot.send_message(message.chat.id,
                     text="Выберите роль пользователя на портале", reply_markup=markup)
    




@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, 'Функция в разработке, извините :(')


bot.polling()
