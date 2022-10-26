
import telebot
from telebot import types # для указание типов
#import export_data
#import import_data

bot = telebot.TeleBot('YOU_TOKEN', parse_mode=None)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Внести новый контакт ✅")
    btn2 = types.KeyboardButton("Вывести список контактов 🗒️")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! \nЯ Телефонныый Бот 🤪".format(message.from_user), reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def func1(message):
    if(message.text == "Внести новый контакт ✅"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("С новой строки")
        btn2 = types.KeyboardButton("В одну строку")
        back = types.KeyboardButton("Вернуться в главное меню ⭐️")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выбирай...", reply_markup=markup)    
    
    elif(message.text == "С новой строки"):
        entry = []
        bot.send_message(message.chat.id, "Введи Фамилию:")
        surname = message.text
        entry.append(surname)
        bot.send_message(message.chat.id, "Введи Имя:")
        name = message.text
        entry.append(name)
        bot.send_message(message.chat.id, 'Введи телефон:')
        phone = message.text
        entry.append(phone)
        bot.send_message(message.chat.id, "Введи описание:")
        description = message.text
        entry.append(description)
        bot.send_message(message.chat.id, "Запись сделана ✅")
        #import_data.input_format1(entry)
        
    elif(message.text == "В одну строку"):
        entry = []
        bot.send_message(message.chat.id, "Введи Фамилию:")
        surname = message.text
        entry.append(surname)
        bot.send_message(message.chat.id, "Введи Имя:")
        name = message.text
        entry.append(name)
        bot.send_message(message.chat.id, 'Введи телефон:')
        phone = message.text
        entry.append(phone)
        bot.send_message(message.chat.id, "Введи описание:")
        description = message.text
        entry.append(description)
        bot.send_message(message.chat.id, "Запись сделана ✅")
        #import_data.input_format2(entry)

    elif(message.text == "Вывести список контактов 🗒️"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("В столбик")
        btn2 = types.KeyboardButton("В строку")
        back = types.KeyboardButton("Вернуться в главное меню ⭐️")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Выбирай...", reply_markup=markup)

    elif(message.text == "В столбик"):
        bot.send_message(message.chat.id, "✅")
        #export_data.read_all_file1()
  
    elif(message.text == "В строку"):
        bot.send_message(message.chat.id, "✅")
        #export_data.read_all_file2()
 
    elif(message.text == "Вернуться в главное меню ⭐️"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("Внести новый контакт ✅")
        button2 = types.KeyboardButton("Вывести список контактов 🗒️")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="⭐️Вы вернулись в главное меню⭐️", reply_markup=markup)
    
    '''else:
        bot.send_message(message.chat.id, text="Такой команды нет! 😔")'''

bot.polling(none_stop=True)
