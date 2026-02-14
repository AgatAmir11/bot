import telebot
import os
TOKEN = os.environ.get("TOKEN")

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "سلام 👋 نظرتو بفرست")

@bot.message_handler(func=lambda message: True)
def get_message(message):
    admin_id = 1086459356 
    bot.send_message(admin_id, f"پیام جدید:\n{message.text}")
    bot.reply_to(message, "✅ ارسال شد")

bot.infinity_polling()





