import telebot
import parser

bot = telebot.TeleBot("")

@bot.message_handler(commands=['info', 'help'])
def send_welcome(message):
	bot.reply_to(message, "https://gs1.com.ua/objects/41-zhk-levada2")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'комендант':
        bot.reply_to(message,'Наш комендант Ольга,тел. 094-977-26-52')
    elif message.text == 'Комендант':
        bot.reply_to(message, 'Наш комендант Ольга,тел. 094-977-26-52')
bot.polling()
