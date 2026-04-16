import telebot
import os  # Bu mütləq olmalıdır

bot = telebot.TeleBot("8761885391:AAGod_5nwQxzwbqI7h1ZsqwUL0pIwEKwCDM")

@bot.message_handler(content_types=['video'])
def handle_video(message):
    # ... videonu yükləmə kodun burda ...
    # ... videonu göndərmə kodun:
    bot.send_video(message.chat.id, open("video.mp4", "rb"))

    # GÖNDƏRDİKDƏN SONRA SİLMƏK ÜÇÜN:
    os.remove("video.mp4") # Bu sətir serverin yaddaşını təmiz saxlayır
worker: python telegram_bot.py