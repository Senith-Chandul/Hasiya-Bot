import os
import telebot

bot = telebot. TeleBot ("1994074376:AAFFQCkCw2zKVu5d48gshrgwbitELMTccJs")

@bot.message_handler("commands=["start"])
def send welcome(message):
    bot.reply_to(message,"Hello i'm Hasiya Chat Bot")

@bot.message_handler(commands=["how"])
def send_message(message):
    bot.send_message(message, "https://google.com")

    bot.polling()
    
