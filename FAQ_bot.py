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

bot = telebot.TeleBot('6714731566:AAHApxAwpfiPsan-VXQJwUOEV0bA9lfvFP4')
bot.remove_webhook()
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
        button1 = InlineKeyboardButton("Поступление/зачисление", callback_data="button_input")
        button2 = InlineKeyboardButton("Лето в детском саду", callback_data="button_zamdir")
        button3 = InlineKeyboardButton("Организационные вопросы. 2024-2025 учебный год", callback_data="button_MFC")
        button4 = InlineKeyboardButton("МФЦ", callback_data="button_DO")
        button5 = InlineKeyboardButton("Прочие вопросы/задать вопрос в чате", callback_data="button_eat")
        markup.add(button1, button2, button3, button4, button5)
        
        bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)
        
    def input_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button1 = InlineKeyboardButton("Детский сад (дошкольное отделение)", callback_data="button_input_1")
        button2 = InlineKeyboardButton("Поступление в 1 класс", callback_data="button_input_2")
        button3 = InlineKeyboardButton("Поступление в 10 класс", callback_data="button_input_3")
        button4 = InlineKeyboardButton("Перевод во 2-11 классы", callback_data="button_input_4")
        button5 = InlineKeyboardButton('На mos.ru пришел ответ "готов к зачислению". Что дальше?', callback_data="button_input_5")
        button6 = InlineKeyboardButton("Что купить?", callback_data="button_input_6")
        button6 = InlineKeyboardButton("Задать вопрос старшему воспитателю/администрации", callback_data="button_input_6")
        button_back = InlineKeyboardButton("Назад", callback_data="button_back")
        markup.add(button1, button2, button3, button4, button5, button6, button_back)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)
        
    def leto_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button1 = InlineKeyboardButton("График работы дошкольных площадок", callback_data="button_leto_1")
        button2 = InlineKeyboardButton("Задать вопрос старшему воспитателю/администрации", callback_data="button_leto_2")
        button_back = InlineKeyboardButton("Назад", callback_data="button_back")
        markup.add(button1, button2, button_back)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)

    def new_year_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button1 = InlineKeyboardButton("График каникул", callback_data="button_year_1")
        button2 = InlineKeyboardButton("1 сентября / День знаний", callback_data="button_year_2")
        button3 = InlineKeyboardButton("Родительские собрания/знакомство с новыми учителями", callback_data="button_year_3")
        button4 = InlineKeyboardButton("Подвоз (школьный автобус)", callback_data="button_year_4")
        button5 = InlineKeyboardButton("Будет ли 2-я смена", callback_data="button_year_5")
        button6 = InlineKeyboardButton("Открытие новых образовательных площадок", callback_data="button_year_6")
        markup.add(button1, button2, button3, button4, button5, button6)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)

    def MFC_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button01 = InlineKeyboardButton("Поступление в 1-класс", callback_data="button_MFC_01")
        button02 = InlineKeyboardButton("Как перевести ребенка во 2-11 класс", callback_data="button_MFC_02")
        button1 = InlineKeyboardButton("Контакты специалистов", callback_data="button_MFC_1")
        button2 = InlineKeyboardButton("График приема", callback_data="button_MFC_2")
        button3 = InlineKeyboardButton("Как распределяются классы?", callback_data="button_MFC_3")
        button4 = InlineKeyboardButton("Можно ли выбрать площадку самостоятельно?", callback_data="button_MFC_4")
        button5 = InlineKeyboardButton("Как отчислить из школы?", callback_data="button_MFC_5")
        button6 = InlineKeyboardButton("Как поменять образовательную площадку?", callback_data="button_MFC_6")
        button7 = InlineKeyboardButton("Как поменять класс в пределах одной параллели?", callback_data="button_MFC_7")
        button8 = InlineKeyboardButton("Как перевестись из одной школьной площадки в другую?", callback_data="button_MFC_8")
        button9 = InlineKeyboardButton("Как получить справку о том, что ребенок учится в школе?", callback_data="button_MFC_9")
        button10 = InlineKeyboardButton("Как получить выписку оценок?", callback_data="button_MFC_10")
        button11 = InlineKeyboardButton("Не работает ЭЖД ребенка, как получить доступ?", callback_data="button_MFC_11")
        button12 = InlineKeyboardButton("Не работает ЭЖД родителя, как получить доступ?", callback_data="button_MFC_12")
        button_back = InlineKeyboardButton("Назад", callback_data="button_back")
        markup.add(button01, button02, button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12, button_back)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)

    def question_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button01 = InlineKeyboardButton("Поступление в 1-класс", callback_data="button_MFC_01")
        button02 = InlineKeyboardButton("Как перевести ребенка во 2-11 класс", callback_data="button_MFC_02")
        button1 = InlineKeyboardButton("Контакты специалистов", callback_data="button_MFC_1")
        button2 = InlineKeyboardButton("График приема", callback_data="button_MFC_2")
        markup.add(button01, button02, button1, button2)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)

    #Функция старт
    @bot.message_handler(commands=['start'])
    def start(message):
        main_menu(message)
        
    #Кнопка Директор
    @bot.callback_query_handler(func=lambda call: call.data == "button_input")
    def handle_callback(call):
        input_menu(call.message)
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
        bot.send_message(call.message.chat.id, '[Example Website](https://example.com)', parse_mode='Markdown')
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