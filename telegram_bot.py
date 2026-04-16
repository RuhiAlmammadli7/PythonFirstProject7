import os
import time
import logging
import yt_dlp
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes

logging.basicConfig(level=logging.INFO)

TOKEN = "8761885391:AAGod_5nwQxzwbqI7h1ZsqwUL0pIwEKwCDM"

user_urls = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Salam, qadanalım! Mənə Instagram, TikTok və ya YouTube linki göndər! 🎬🎵"
    )

async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()

    valid = any(x in url for x in ["instagram.com", "tiktok.com", "youtube.com", "youtu.be"])
    if not valid:
        await update.message.reply_text("❌ Qadası, düzgün link göndər.")
        return

    user_urls[update.message.from_user.id] = url

    keyboard = [
        [
            InlineKeyboardButton("🎬 Video (MP4)", callback_data="video"),
            InlineKeyboardButton("🎵 Səs (MP3)", callback_data="audio"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Nə yükləyim?", reply_markup=reply_markup)

async def handle_choice(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    user_id = query.from_user.id
    url = user_urls.get(user_id)

    if not url:
        await query.edit_message_text("❌ Link tapılmadı, yenidən göndər.")
        return

    choice = query.data
    await query.edit_message_text("⏳ Yüklənir qadası, gözlə...")

    output_path = f"file_{user_id}_{int(time.time())}"

    if choice == "video":
        ydl_opts = {
            "outtmpl": output_path + ".mp4",
            "format": "best[ext=mp4]/best",
            "quiet": False,
        }
        file_path = output_path + ".mp4"
    else:
        ydl_opts = {
            "outtmpl": output_path + ".mp3",
            "format": "bestaudio/best",
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "quiet": False,
        }
        file_path = output_path + ".mp3"

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        file_size = os.path.getsize(file_path)
        if file_size > 50 * 1024 * 1024:
            await query.edit_message_text("❌ Fayl çox böyükdür (50MB+). Daha qısa video seç.")
            return

        await query.edit_message_text("📤 Göndərilir...")

        with open(file_path, "rb") as f:
            if choice == "video":
                await query.message.reply_video(video=f)
            else:
                await query.message.reply_audio(audio=f)

        await query.delete_message()

    except Exception as e:
        await query.edit_message_text(f"❌ Xəta: {str(e)}")
        logging.error(f"Xəta: {e}")

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))
    app.add_handler(CallbackQueryHandler(handle_choice))
    app.run_polling()