import telebot
from secret import token
from telebot import types
from datetime import datetime

all_content_types = ["text", "audio", "document", "photo", "sticker", "video", "video_note", "voice", "location", "contact",
                 "new_chat_members", "left_chat_member", "new_chat_title", "new_chat_photo", "delete_chat_photo",
                 "group_chat_created", "supergroup_chat_created", "channel_chat_created", "migrate_to_chat_id",
                 "migrate_from_chat_id", "pinned_message"]

tooday_datetime = datetime.now()
bot = telebot.TeleBot(token)

def make_str(ready):
    a_str = "".join(ready)
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
        try:
            file = open('my_list.txt')
            a_list = []
            for i in file:
                a_list.append(i)
            file.close()
            bot.send_message(message.chat.id, make_str(a_list))
        except:
            bot.send_message(message.chat.id, 'У вас нет выполненных дел')
            f1 = open('my_list_2.txt', 'a')
            file.close()
    elif message.text == 'Не выполненные дела':
        try:
            file_2 = open('my_list_2.txt')
            a_list_2 = []
            for i in file_2:
                a_list_2.append(i)
            file_2.close()
            bot.send_message(message.chat.id, make_str(a_list_2))
        except:
            bot.send_message(message.chat.id, 'У вас нет дел')
    
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
    f1 = open('my_list_2.txt', 'a')
    a = message.text
    f1.write(a + '\n')
    f1.close()
    bot.send_message(message.chat.id,'Добавлено!')

def user_input_2(message):
    f1 = open('my_list.txt', 'a')
    a = message.text
    f1.write(a + '\n')
    f1.close()
    bot.send_message(message.chat.id,'Добавлено!')
#_______________________________________________________________________________________

@bot.message_handler(content_types=all_content_types)
def audio_user(message):
    if message.content_type == 'voice':
        bot.send_photo(message.chat.id, open('screenshot_18-2.png', 'rb'))
        bot.send_message(message.chat.id, 'Чего блин?\nЯ не могу распознать эту запись')
#_______________________________________________________________________________________
bot.polling(none_stop=True)