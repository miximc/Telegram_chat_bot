import telebot
from secret import token
from telebot import types
from datetime import datetime


ready_list = []
not_ready_list = []
tooday_datetime = datetime.now()
bot = telebot.TeleBot(token)



def qwe(ready):
    a = "".join(ready)
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
def user(message):
    global a
    if message.text == 'Время и дата':
        bot.send_message(
            message.chat.id,
            f'Сегодня:\n{tooday_datetime.now()}')
    elif message.text == 'Дела':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton('Выполненные дела')
        btn2 = types.KeyboardButton('Не выполненные дела')
        btn3 = types.KeyboardButton('Добавить выполненное дело')
        btn4 = types.KeyboardButton('Добавить дело')  
        markup.add(btn1, btn2, btn3,btn4)
        bot.send_message(message.chat.id, 'Выберете что вы хотите сделать:', reply_markup=markup) 
    elif message.text == 'Выполненные дела':
        try:
            file = open('my_list.txt')
            a = []
            for i in file:
                a.append(i)
            print(a)
            file.close()
            bot.send_message(message.chat.id, qwe(a))
        except:
            bot.send_message(message.chat.id, 'Нет такого файла')
            print('Такого файла нет или нет выполненных дел')
    elif message.text == 'Не выполненные дела':
        try:
            file_2 = open('my_list_2.txt')
            a = []
            for i in file_2:
                a.append(i)
            print(a)
            file_2.close()
            bot.send_message(message.chat.id, qwe(a))
        except:
            bot.send_message(message.chat.id, 'Нет такого файла')
            print('Такого файла нет или нет выполненных дел')
    
    elif message.text == 'Добавить дело':
        
        mesg = bot.send_message(message.chat.id,'Введите ваше дело:')
        bot.register_next_step_handler(mesg,user_input)
def user_input(message):
    f1 = open('my_list_2.txt', 'a')
    a = message.text
    f1.write(a + '\n')
    f1.close()
    bot.send_message(message.chat.id,'Добавлено!')



            
            
        
                
bot.polling(none_stop=True)