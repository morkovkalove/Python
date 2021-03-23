import telebot
import config
import random

from telebot import types

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti  = open('static/welcome.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    
    # keyboard
    markup = types.ReplyKeyboardMarkup(resiz_keyboard=True)
    item1 = types.KeyboardButton("Рандомное число")
    item2 = types.KeyboardButton("Как дела?")
    
    markup.add(item1, item2)
    
    bot.send_message(message.chat.id, 'Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть подопытным кроликом.'.format(message.from_user, bot.get_me()),
    parse_mode = 'html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def privetiki(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == 'Как дела?':
            bot.send_message(message.chat.id, 'Всё супер! А у тебя как?')
        else:
            bot.send_message(message.chat.id, 'Я не знаю что и ответить..хнык')
    
# RUN
bot.polling(none_stop = True)