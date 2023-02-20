import telebot
from secret import token
from telebot import types
from datetime import datetime







ready_list = []
not_ready_list = []
tooday_datetime = datetime.now()
bot = telebot.TeleBot(token)

def qwe(ready):
    a = "\n".join(ready)
    return a   
#___________________________________________________________________________
@bot.message_handler(commands=['start'])
def start(message):
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton('Время и дата')
    btn2 = types.KeyboardButton('Дела')  
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Hi!', reply_markup=markup)
#___________________________________________________________________________
@bot.message_handler(content_types=['text'])
def func(message):
    
    if message.text == 'Время и дата':
        bot.send_message(
            message.chat.id,
            f'Сегодня:\n {tooday_datetime.now()}')
    elif message.text == 'Дела':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Посмотреть выполненные дела')
        btn2 = types.KeyboardButton('Посмотреть не выполненные дела')
        btn3 = types.KeyboardButton('Добавить выполненное дело')
        btn4 = types.KeyboardButton('Добавить не выполненное дело')  
        markup.add(btn1, btn2, btn3,btn4)
        bot.send_message(message.chat.id, 'Выберете что вы хотите сделать:', reply_markup=markup)



    if message.text == 'Посмотреть выполненные дела':
        b = []
        my_file = open('my_list.txt', 'a+')
        for i in my_file:
            b.append(i)
        print('try')
        bot.send_message(
            message.chat.id,
            f'Вы сделали следующие дела:\n{b}')

    elif message.text == 'Посмотреть не выполненные дела':
        bot.send_message(
            message.chat.id,
            f'Вам остались следующие дела:\nNone'
        )
    # elif message.text == 'Добавить выполненное дело':
    #     mesg = bot.send_message(message.chat.id,'Введите ваше дело:')
    #     bot.register_next_step_handler(mesg,user_input)
# @bot.message_handler(content_types=['text'])
# def user_input(message):
#     a = message.text
    
#     my_file = open('my_list.txt', 'a+')
#     print('file open')
#     my_file.write(a + '\n')
#     my_file.close()
#     # except IOError:
#     #     my_file = open('my_list.txt','w+')
#     #     my_file.write(a + '\n')
#     #     my_file.close()
#     ready_list.append(a)
#     bot.send_message(message.chat.id,'Добавлено!')
#     if a in not_ready_list:
#         not_ready_list.remove(a)         


bot.polling(none_stop=True)