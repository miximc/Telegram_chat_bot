from secret import token
import telebot 
from datetime import datetime

tooday_datetime = datetime.now()
ready_list = ['Покушать', 'Поспать', 'Полежать']

not_ready_list = ['Поработать','Поучиться','Посмотреть кино']

my_command = 'Мои команды:\n "/время" - дата и время суток \n "/сделано" - выполненные дела\n "/остаток" - не выполненные дела'

tooday  = datetime.date

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    print('I\'m you\'r new bot')
    bot.send_message(
        message.chat.id,
        f'Приветствую! \n {my_command}' ,
        parse_mode='html'
    )

@bot.message_handler(commands=['время'])
def date_now(message):
    bot.send_message(
        message.chat.id,
        f'Дата: {tooday_datetime.date()}\nВремя: {tooday_datetime.hour}:{tooday_datetime.minute}')


@bot.message_handler(commands=['сделано'])
def ready(message):
    print(*ready_list)
    bot.send_message(
        message.chat.id,
        f'Вы сделали следующие дела:\n{qwe(ready_list)}'
    )
def qwe(ready):
    a = "\n".join(ready)
    return a       

@bot.message_handler(commands=['остаток'])
def ready(message):
    print(*ready_list)
    bot.send_message(
        message.chat.id,
        f'Вам остались следующие дела:\n{qwe(not_ready_list)}'
    )
def qwe(ready):
    a = "\n".join(ready)
    return a       

bot.polling(none_stop=True)
