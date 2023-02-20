import telebot
from secret import token
from telebot import types
from datetime import datetime

ready_list = ['Покушать', 'Поспать', 'Полежать']

not_ready_list = ['Поработать','Поучиться','Посмотреть кино']
tooday_datetime = datetime.now()
bot = telebot.TeleBot(token)

def qwe(ready):
    a = "\n".join(ready)
    return a   

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Время и дата')
    btn2 = types.KeyboardButton('Выполненные дела')
    btn3 = types.KeyboardButton('Список не выполненного')
    btn4 = types.KeyboardButton('Добавить выполненное дело')  
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Hi!', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    
    if message.text == 'Время и дата':
        bot.send_message(
            message.chat.id,
            f'Сегодня:\n {tooday_datetime.now()}')

    elif message.text == 'Выполненные дела':
        bot.send_message(
            message.chat.id,
            f'Вы сделали следующие дела:\n{qwe(ready_list)}')

    elif message.text == 'Список не выполненного':
        bot.send_message(
            message.chat.id,
            f'Вам остались следующие дела:\n{qwe(not_ready_list)}'
        )
    elif message.text == 'Добавить выполненное дело':
        mesg = bot.send_message(message.chat.id,'Введите ваше дело:')
        bot.register_next_step_handler(mesg,user_input)
def user_input(message):
    a = message.text
    ready_list.append(a)
    bot.send_message(message.chat.id,'Добавлено!')
    if a in not_ready_list:
        not_ready_list.remove(a)         


bot.polling(none_stop=True)