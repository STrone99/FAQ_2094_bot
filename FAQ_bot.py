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

user_chat = {}

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
        button1 = InlineKeyboardButton("Поступление/зачисление", callback_data="button_main_1")
        button2 = InlineKeyboardButton("Лето в детском саду", callback_data="button_main_2")
        button3 = InlineKeyboardButton("Доступ на территорию школы в летний период", callback_data="button_main_3")
        button4 = InlineKeyboardButton("Организационные вопросы. 2024-2025 учебный год", callback_data="button_main_4")
        button5 = InlineKeyboardButton("МФЦ", callback_data="button_main_5")
        button6 = InlineKeyboardButton("Адреса и телефоны", callback_data="button_main_6")
        button7 = InlineKeyboardButton("Прочие вопросы/задать вопрос в чате", callback_data="button_main_7")
        markup.add(button1, button2, button3, button4, button5, button6, button7)
        
        bot.send_message(message.chat.id, "Выберите раздел:", reply_markup=markup)
        
    def input_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button1 = InlineKeyboardButton("Детский сад (дошкольное отделение)", callback_data="button_input_1")
        button2 = InlineKeyboardButton("Поступление в 1 класс", callback_data="button_input_2")
        button3 = InlineKeyboardButton("Поступление в 10 класс", callback_data="button_input_3")
        button4 = InlineKeyboardButton("Перевод во 2-11 классы", callback_data="button_input_4")
        button5 = InlineKeyboardButton('Что означает статус заявления на mos.ru', callback_data="button_input_5")
        button6 = InlineKeyboardButton("Что купить?", callback_data="button_input_6")
        button7 = InlineKeyboardButton("Задать вопрос старшему администрации", callback_data="button_input_6")
        button_back = InlineKeyboardButton("Назад", callback_data="button_back")
        markup.add(button1, button2, button3, button4, button5, button6, button7, button_back)
        
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
        button2 = InlineKeyboardButton("1 сентября/День знаний", callback_data="button_year_2")
        button3 = InlineKeyboardButton("Родительские собрания/знакомство с новыми учителями", callback_data="button_year_3")
        button4 = InlineKeyboardButton("Доступ на территорию", callback_data="button_year_4")
        button5 = InlineKeyboardButton("Направления обучения", callback_data="button_year_5")
        button6 = InlineKeyboardButton("Карта “Москвенок”", callback_data="button_year_6")
        button7 = InlineKeyboardButton("ЭЖД", callback_data="button_year_7")
        button8 = InlineKeyboardButton("Питание", callback_data="button_year_8")
        button9 = InlineKeyboardButton("Когда откроется запись в кружки и секции", callback_data="button_year_9")
        button10 = InlineKeyboardButton("Дополнительное образование", callback_data="button_year_10")
        button11 = InlineKeyboardButton("Подвоз (школьный автобус)", callback_data="button_year_11")
        button12 = InlineKeyboardButton("Хотим перевестись", callback_data="button_year_12")
        button13 = InlineKeyboardButton("Будет ли 2-я смена?", callback_data="button_year_13")
        button14 = InlineKeyboardButton("Открытие новых образовательных площадок", callback_data="button_year_14")
        button_back = InlineKeyboardButton("Назад", callback_data="button_back")
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, 
                   button11, button12, button13, button14, button_back)
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)

    def MFC_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button1 = InlineKeyboardButton("График работы МФЦ, контакты", callback_data="button_MFC_1")
        button2 = InlineKeyboardButton("Получить справку/выписку/характеристику", callback_data="button_MFC_2")
        button3 = InlineKeyboardButton("Отчислиться из школы", callback_data="button_MFC_3")
        button4 = InlineKeyboardButton("Оставить жалобу", callback_data="button_MFC_4")
        button5 = InlineKeyboardButton("Обратиться с предложением", callback_data="button_MFC_5")
        button6 = InlineKeyboardButton("Оставить отзыв", callback_data="button_MFC_6")
        button7 = InlineKeyboardButton("Записаться на прием к директору", callback_data="button_MFC_7")
        button8 = InlineKeyboardButton("Задать другой вопрос", callback_data="button_MFC_8")
        button_back = InlineKeyboardButton("Назад", callback_data="button_back")
        markup.add( button1, button2, button3, button4, button5, button6, button7, button8, button_back)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)

    def question_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button01 = InlineKeyboardButton("Поступление в 1-класс", callback_data="button_MFC_01")
        button02 = InlineKeyboardButton("Как перевести ребенка во 2-11 класс", callback_data="button_MFC_02")
        button1 = InlineKeyboardButton("Контакты специалистов", callback_data="button_MFC_1")
        button2 = InlineKeyboardButton("График приема", callback_data="button_MFC_2")
        markup.add(button01, button02, button1, button2)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)

    def dopobr_menu(message):
        markup = InlineKeyboardMarkup(row_width=1)
        button1 = InlineKeyboardButton("Контакты службы дополнительного образования", callback_data="button_dopobr_1")
        button2 = InlineKeyboardButton("Выбрать кружки/секции для записи", callback_data="button_dopobr_2")
        button3 = InlineKeyboardButton("Расписание занятий допобразования", callback_data="button_dopobr_3")
        button4 = InlineKeyboardButton("Как зачислить ребенка в кружок/ секцию", callback_data="button_dopobr_4")
        button5 = InlineKeyboardButton("Как отчислить ребенка из кружка/ секции", callback_data="button_dopobr_5")
        button6 = InlineKeyboardButton("Как заключить договор", callback_data="button_dopobr_6")
        button7 = InlineKeyboardButton("Как расторгнуть договор", callback_data="button_dopobr_7")
        button8 = InlineKeyboardButton("Перечень и стоимость кружков и секций", callback_data="button_dopobr_8")
        button9 = InlineKeyboardButton("Из чего складывается стоимость занятий", callback_data="button_dopobr_9")
        button10 = InlineKeyboardButton("Как осуществить оплату", callback_data="button_dopobr_10")
        button11 = InlineKeyboardButton("Как сделать перерасчет выставленной квитанции", callback_data="button_dopobr_11")
        button12 = InlineKeyboardButton("За что производится перерасчет", callback_data="button_dopobr_12")
        button13 = InlineKeyboardButton("С какого момента после заключения договора начисляется оплата", callback_data="button_dopobr_13")
        button14 = InlineKeyboardButton("Льготы", callback_data="button_dopobr_14")
        button15 = InlineKeyboardButton("Оплата занятий материнским капиталом", callback_data="button_dopobr_15")
        button16 = InlineKeyboardButton("Получение налогового вычета за оплату занятий", callback_data="button_dopobr_16")
        button17 = InlineKeyboardButton("Обратиться с жалобой на работу педагога/тренера", callback_data="button_dopobr_17")
        button18 = InlineKeyboardButton("Задать другой вопрос", callback_data="button_dopobr_18")
        button_back = InlineKeyboardButton("Назад", callback_data="button_back")
        markup.add( button1, button2, button3, button4, button5, button6, button7, button8, button9, 
                   button10, button11, button12, button13, button14, button15, button16, button17, button18, button_back)
        
        bot.send_message(message.chat.id, "Выберите ваш вопрос:", reply_markup=markup)
    try:
        #Функция старт
        @bot.message_handler(commands=['start'])
        def start(message):
            user_chat[message.chat.id] = 'main'
            main_menu(message)
        #!Обработка кнопок главного меню
        @bot.callback_query_handler(func=lambda call: call.data == "button_main_1")
        def handle_callback(call):
            input_menu(call.message)
            bot.delete_message(call.message.chat.id, call.message.message_id)
        @bot.callback_query_handler(func=lambda call: call.data == "button_main_2")
        def handle_callback(call):
            leto_menu(call.message)
            bot.delete_message(call.message.chat.id, call.message.message_id)
        @bot.callback_query_handler(func=lambda call: call.data == "button_main_3")
        def handle_callback(call):
            bot.delete_message(call.message.chat.id, call.message.message_id)  
            bot.send_message(call.message.chat.id, "Отвественный за этот вопрос пока не предоставил информацию о нём😭😭😭\n\n*Чтобы вернуться в основное меню нажмите на* /start", parse_mode='Markdown')
        @bot.callback_query_handler(func=lambda call: call.data == "button_main_4")
        def handle_callback(call):
            new_year_menu(call.message)
            bot.delete_message(call.message.chat.id, call.message.message_id)
        @bot.callback_query_handler(func=lambda call: call.data == "button_main_5")
        def handle_callback(call):
            MFC_menu(call.message)
            bot.delete_message(call.message.chat.id, call.message.message_id)
        @bot.callback_query_handler(func=lambda call: call.data == "button_main_7")
        def handle_callback(call):
            user_chat[call.message.chat.id] = ('question_main')
            bot.send_message(call.message.chat.id, "Напишите ваш вопрос\n\n*Чтобы вернуться в основное меню нажмите на* /start", parse_mode='Markdown')
        @bot.message_handler(func=lambda message: True)
        def receive_message(message):
            if user_chat[message.chat.id] == 'question_main':
                markup = InlineKeyboardMarkup()
                button = InlineKeyboardButton(text="Ответить", callback_data=f"reply_{message.chat.id}_{message.message_id}_{message.from_user.username}")
                markup.add(button)
                
                bot.send_message('-1002230522864', f"Сообщение от пользователя @{message.from_user.username}:\n\n{message.text}", reply_markup=markup)
                bot.send_message(message.chat.id, "Ваше сообщение успешно отправлено!", parse_mode='Markdown')
                user_chat[message.chat.id] = 'main'
            else:
                bot.send_message(message.chat.id, "Незнакомая команда!\n\n*Чтобы вернуться в основное меню нажмите на* /start", parse_mode='Markdown')
        @bot.callback_query_handler(func=lambda call: call.data.startswith("reply_"))
        def handle_callback_query(call):
            _, user_id, original_message_id, nick = call.data.split('_')
            bot.send_message(call.message.chat.id, f"Введите ваш ответ для пользователя @{nick}:")

            bot.register_next_step_handler(call.message, forward_response, user_id, original_message_id)

        def forward_response(message, user_id, original_message_id):
            bot.send_message(user_id, f"*Ответ на ваше сообщение:*\n{message.text}", parse_mode='Markdown')
            bot.send_message('-1002230522864', f"Ответ отправлен пользователю @{message.from_user.username}")
    except Exception as e:
        print(e)
        
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