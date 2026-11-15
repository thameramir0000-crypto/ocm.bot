from flask import Flask
import threading
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# --- باش ما يحبسش ---
app = Flask(__name__)
@app.route('/')
def home():
    return "Youssef Bot is Alive!"

def run_flask():
    app.run(host="0.0.0.0", port=8080)
threading.Thread(target=run_flask).start()
# --------------------

TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🌟 OCM-201", callback_data="ocm")],
        [InlineKeyboardButton("👤 حسابي", callback_data="account"), InlineKeyboardButton("💳 شحن", callback_data="charge")],
        [InlineKeyboardButton("📞 دعم", callback_data="support")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "مرحبا بيك عند يوسف بوت 🌟\n\nواش تحب دير؟",
        reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "ocm":
        await query.edit_message_text("🔥 OCM-201 متوفر دوك\nالسعر: ...\nللطلب كليكي على شحن")
    elif query.data == "account":
        await query.edit_message_text(f"👤 حسابك:\nID: {query.from_user.id}\nالاسم: {query.from_user.first_name}\nرصيدك: 0 DA")
    elif query.data == "charge":
        await query.edit_message_text("💳 باش تشحن ابعث لـ @youssef و قولو شحال حاب تشحن")
    elif query.data == "support":
        await query.edit_message_text("📞 الدعم: @youssef")

def main():
    app_bot = ApplicationBuilder().token(TOKEN).build()
    app_bot.add_handler(CommandHandler("start", start))
    app_bot.add_handler(CallbackQueryHandler(button))
    print("Youssef Bot started...")
    app_bot.run_polling()

if __name__ == "__main__":
    main()
