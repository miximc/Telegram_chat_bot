from Telegram_chat_bot.secret import token
import telebot 
from datetime import datetime


tooday_datetime = datetime.now()
ready_list = ['Покушать', 'Поспать', 'Полежать']

not_ready_list = ['Поработать','Поучиться','Посмотреть кино']

my_command = 'Я умею:\n1. Показывать время - "время" \n2. Показывать выполненные дела - "сделано"\n3. Показывать не выполненные дела- "остаток"'

tooday = datetime.date

bot = telebot.TeleBot(token)

def qwe(ready):
    a = "\n".join(ready)
    return a    

@bot.message_handler(commands=['start'])
def start(message):
    print('I\'m you\'r new bot')
    bot.send_message(
        message.chat.id,
        f'Приветствую! \n {my_command}'
    )

@bot.message_handler(content_types=['text'])
def date_now(message):
    user_text = message.text
    if user_text.lower() == 'время':
        bot.send_message(
            message.chat.id,
            f'Сегодня:\n {tooday_datetime.now()}')

    elif user_text.lower() == 'сделано':
        bot.send_message(
            message.chat.id,
            f'Вы сделали следующие дела:\n{qwe(ready_list)}')

    elif user_text.lower() == 'остаток':
        bot.send_message(
            message.chat.id,
            f'Вам остались следующие дела:\n{qwe(not_ready_list)}'
        )
    else:
        bot.send_message(
            message.chat.id,
            'Я не знаю ответа на ваш вопрос! :('
        )
   
       

bot.polling(none_stop=True)
