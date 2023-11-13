import telebot
import os
from telebot import types
from currency_converter import CurrencyConverter

TgToken = os.getenv("TG_TOKEN")
bot = telebot.TeleBot(TgToken)
currency = CurrencyConverter()
ammount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, введите сумму")
    bot.register_next_step_handler(message, summa)


def summa(message):
    global ammount
    ammount = message.text.strip()

    murkup = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
    btn2 = types.InlineKeyboardButton('Eur/Usd', callback_data='usd/eur')
    btn3 = types.InlineKeyboardButton('Usd/Gbr', callback_data='usd/eur')
    btn4 = types.InlineKeyboardButton('другое значение', callback_data='usd/eur')



bot.polling(none_stop=True)
