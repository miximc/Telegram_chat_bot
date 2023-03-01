import telebot
import sqlite3
from secret import token
from telebot import types
from datetime import datetime
#________________________________
comm = sqlite3.connect('bd_bot_v2.sqlite3')
cursor = comm.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS tasks(
    id INTEGER,
    name VARCHAR(50), status VARCHAR(20), PRIMARY KEY (id))''')
cursor.close()
all_content_types = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"]

tooday_datetime = datetime.now()
bot = telebot.TeleBot(token)

def make_str(ready):
    a_str = "\n".join(ready)
    return a_str   

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
        btn5 = types.KeyboardButton('Удалить все дела')  
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'Выберете что вы хотите сделать:', reply_markup=markup) 

    elif message.text == 'Выполненные дела':
        comm = sqlite3.connect('bd_bot.sqlite3')
        cursor = comm.cursor()
        vals_completed = cursor.execute('SELECT * FROM completed_tasks')
        comp_tasks = []
        for i in vals_completed:
            a_str = "".join(i[1])
            comp_tasks.append(a_str)
            print(i, type(i))
        bot.send_message(message.chat.id, make_str(comp_tasks))
        
    elif message.text == 'Не выполненные дела':
        comm = sqlite3.connect('bd_bot_v2.sqlite3')
        cursor = comm.cursor()
        vals_uncompleted = cursor.execute('SELECT name FROM tasks')
        uncomp_tasks = []
        print(vals_uncompleted)  
        for i in vals_uncompleted:
            b_str = "".join(i)
            uncomp_tasks.append(b_str)
            print(i, type(i))
            
        bot.send_message(message.chat.id, make_str(uncomp_tasks))
    
    elif message.text == 'Добавить дело':
        mesg = bot.send_message(message.chat.id,'Введите ваше дело:')
        bot.register_next_step_handler(mesg, user_input)

    elif message.text == 'Добавить выполненное дело':
        mesg = bot.send_message(message.chat.id,'Введите ваше дело:')
        bot.register_next_step_handler(mesg, user_input_2)
    elif message.text == 'Удалить все дела':
        f1 = open('my_list_2.txt', 'w')
        f1.close()
        f2 = open('my_list.txt', 'w')
        f2.close()

def user_input(message):
    comm = sqlite3.connect('bd_bot_v2.sqlite3')
    cursor = comm.cursor()
    a = message.text
    request = f'INSERT INTO tasks(name, status) VALUES ("{a}", "невыполненно")'
    cursor.execute(request)
    comm.commit()
    bot.send_message(message.chat.id,'Добавлено!')

def user_input_2(message):
    comm = sqlite3.connect('bd_bot_v2.sqlite3')
    cursor = comm.cursor()
    delo = message.text
    q = cursor.execute('SELECT name FROM tasks')
    w = []
    for i in q:
        e = ''.join(i)
        w.append(e)
    request = f'INSERT INTO tasks(name, status) VALUES ("{delo}","выполненно" )'
    cursor.execute(request)
    comm.commit()

    bot.send_message(message.chat.id,'Добавлено!')
#_______________________________________________________________________________________

@bot.message_handler(content_types=all_content_types)
def audio_user(message):
    if message.content_type == 'voice':
        bot.send_photo(message.chat.id, open('screenshot_18-2.png', 'rb'))
        bot.send_message(message.chat.id, 'Чего блин?\nЯ не могу распознать эту запись')
#_______________________________________________________________________________________
bot.polling(none_stop=True)