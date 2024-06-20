from telebot import types
from datetime import datetime
import telebot
import os
import sqlite3
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

current_directory = os.path.dirname(os.path.abspath(__file__))
database_directory = os.path.join(current_directory, 'database')
database = f'{database_directory}//FAQ_bot.db'
mess_id = None

bot = telebot.TeleBot('7463447667:AAEKdNXJfAIeLTgtErXoeiYdV3zFXAY4a0c')
try:
    class DB():
        def create_db():
            if not os.path.exists(database_directory):
                os.makedirs(database_directory)
            conn = sqlite3.connect(database)
            cursor = conn.cursor()
            cursor.execute('''   CREATE TABLE IF NOT EXISTS school 
            (
                id INTEGER PRIMARY KEY,
                name_school TEXT NOT NULL,
                address TEXT NOT NULL
            )''')
            conn.close()

    def main_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button1 = InlineKeyboardButton("👨‍💼Директор", callback_data="button_dir")
        button2 = InlineKeyboardButton("👩‍💼Заместители директора", callback_data="button_zamdir")
        button3 = InlineKeyboardButton("📎Раздел МФЦ", callback_data="button_MFC")
        button4 = InlineKeyboardButton("👩‍🏫Дополнительное образование", callback_data="button_DO")
        button5 = InlineKeyboardButton("😋Питание", callback_data="button_eat")
        button6 = InlineKeyboardButton("🏫Общее", callback_data="button_all")
        markup.add(button1, button2, button3, button4, button5, button6)
        
        bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)
        
    def dir_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button1 = InlineKeyboardButton("Как попасть на прием к директору?", callback_data="button_dir_1")
        button2 = InlineKeyboardButton("Как задать вопрос директору?", callback_data="button_dir_2")
        button_back = InlineKeyboardButton("Назад", callback_data="button_back")
        markup.add(button1, button2, button_back)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)
        
    def zamdir_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button1 = InlineKeyboardButton("Какие направления курируют заместители директора?", callback_data="button_zamdir_1")
        button2 = InlineKeyboardButton("Как попасть на прием к директору?", callback_data="button_zamdir_2")
        button3 = InlineKeyboardButton("Как задать вопрос директору?", callback_data="button_zamdir_3")
        button_back = InlineKeyboardButton("Назад", callback_data="button_back")
        markup.add(button1, button2, button3, button_back)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)
        
    def MFC_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button01 = InlineKeyboardButton("Поступление в 1-класс", callback_data="button_MFC_01")
        button02 = InlineKeyboardButton("Как перевести ребенка во 2-11 класс", callback_data="button_MFC_02")
        button1 = InlineKeyboardButton("Контакты специалистов", callback_data="button_MFC_1")
        button2 = InlineKeyboardButton("График приема", callback_data="button_MFC_2")
        button3 = InlineKeyboardButton("Как распределяется классы?", callback_data="button_MFC_3")
        button4 = InlineKeyboardButton("Можно ли выбрать площадку самостоятельно?", callback_data="button_MFC_4")
        button5 = InlineKeyboardButton("Как отчислить из школы?", callback_data="button_MFC_5")
        button6 = InlineKeyboardButton("Как поменять образовательную площадку?", callback_data="button_MFC_6")
        button7 = InlineKeyboardButton("Как поменять класс в рамках одной параллели?", callback_data="button_MFC_7")
        button8 = InlineKeyboardButton("Как перевестись из одной школьной площадки в другую?", callback_data="button_MFC_8")
        button9 = InlineKeyboardButton("Как получить справку о том, что ребенок учится в школе?", callback_data="button_MFC_9")
        button10 = InlineKeyboardButton("Как получить выписку оценок?", callback_data="button_MFC_10")
        button11 = InlineKeyboardButton("Не работает ЭЖД ребенка, как получить доступ?", callback_data="button_MFC_11")
        button12 = InlineKeyboardButton("Не работает ЭЖД родителя, как получить доступ?", callback_data="button_MFC_12")
        button_back = InlineKeyboardButton("Назад", callback_data="button_back")
        markup.add(button01, button02, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button_back)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)

    def first_class_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button1 = InlineKeyboardButton("Как узнать своего учителя?", callback_data="button_firstclass_1")
        button2 = InlineKeyboardButton("Можно ли выбрать учителя?", callback_data="button_firstclass_2")
        button3 = InlineKeyboardButton("Набор первоклассника", callback_data="button_firstclass_3")
        button4 = InlineKeyboardButton("Какая программа обучения?", callback_data="button_firstclass_4")
        button_back = InlineKeyboardButton("Назад", callback_data="button_back_MFC")
        markup.add(button1, button2, button3, button4, button_back)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)

    def class_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button1 = InlineKeyboardButton("Как поменять группу по английскому языку?", callback_data="button_class_1")
        button2 = InlineKeyboardButton("Как перевести ребенка во 2-11 класс?", callback_data="button_class_2")
        button3 = InlineKeyboardButton("Как поменять группу по информатике?", callback_data="button_class_3")
        button4 = InlineKeyboardButton("Как поменять класс ?", callback_data="button_class_4")
        button5 = InlineKeyboardButton("Направления обучения с 5-го класса", callback_data="button_class_5")
        button6 = InlineKeyboardButton("Направления обучения с 10-го класса", callback_data="button_class_6")
        button7 = InlineKeyboardButton("Как поменять класс ?", callback_data="button_class_7")
        button_back = InlineKeyboardButton("Назад", callback_data="button_back_MFC")
        markup.add(button1, button2, button3, button4, button5, button6, button7, button_back)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)

    #Функция старт
    @bot.message_handler(commands=['start'])
    def start(message):
        main_menu(message)
        
    #Кнопка Директор
    @bot.callback_query_handler(func=lambda call: call.data == "button_dir")
    def handle_callback(call):
        dir_menu(call.message)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    #Кнопка Заместитель директора
    @bot.callback_query_handler(func=lambda call: call.data == "button_zamdir")
    def handle_callback(call):
        zamdir_menu(call.message)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        
    #Кнопка МФЦ
    @bot.callback_query_handler(func=lambda call: call.data == "button_MFC")
    def handle_callback(call):
        MFC_menu(call.message)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        
    #*Кнопка МФЦ 1 класс
    @bot.callback_query_handler(func=lambda call: call.data == "button_MFC_01")
    def handle_callback(call):
        class_menu(call.message)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        
    #*Кнопка МФЦ 2-9 класс
    @bot.callback_query_handler(func=lambda call: call.data == "button_MFC_02")
    def handle_callback(call):
        MFC_menu(call.message)
        bot.delete_message(call.message.chat.id, call.message.message_id)

    #!Кнопки директора
    @bot.callback_query_handler(func=lambda call: call.data == "button_dir_1")
    def handle_callback(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Здесь будет описание данного пункта!\n\n*Чтобы вернуться в основное меню нажмите на* /start", parse_mode='Markdown')
    @bot.callback_query_handler(func=lambda call: call.data == "button_dir_2")
    def handle_callback(call):
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, "Здесь будет описание данного пункта!\n\n*Чтобы вернуться в основное меню нажмите на* /start", parse_mode='Markdown')

    #?Кнопка Назад
    @bot.callback_query_handler(func=lambda call: call.data == "button_back")
    def handle_callback(call):
        main_menu(call.message)
        bot.delete_message(call.message.chat.id, call.message.message_id)   
    @bot.callback_query_handler(func=lambda call: call.data == "button_back_MFC")
    def handle_callback(call):
        MFC_menu(call.message)
        bot.delete_message(call.message.chat.id, call.message.message_id)
        
    bot.polling()
except Exception as e:
    print(e)