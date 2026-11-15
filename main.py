from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters, ContextTypes
import os
TOKEN = os.environ.get("TOKEN")
PRICES = "💰 OCM-201:\n\n🎬 NETFLIX 600 دج\n📺 SHAHID 500 دج\n🎧 SPOTIFY 400 دج\n🤖 CHATGPT 2000 دج"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎬 Netflix", callback_data="netflix")],[InlineKeyboardButton("💰 الأسعار", callback_data="prices")],[InlineKeyboardButton("💳 الدفع", callback_data="pay")],]
    await update.message.reply_text("مرحبا بيك عند OCM-201-official 🌟", reply_markup=InlineKeyboardMarkup(keyboard))
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "prices":
        await query.message.reply_text(PRICES)
    elif query.data == "netflix":
        await query.message.reply_text("🎬 NETFLIX 600 دج / شهر ✅")
    elif query.data == "pay":
        await query.message.reply_text("💳 BaridiMob / CCP / USDT")
async def reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "سلام" in text or "salam" in text:
        await update.message.reply_text("وعليكم السلام 🌸 اكتب /start")
        return
    if "سعر" in text or "شحال" in text:
        await update.message.reply_text(PRICES)
        return
    await update.message.reply_text("شكرا رسالتك وصلت ✅ اكتب /start")
def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply))
    print("البوت يمشي...")
    app.run_polling()
main()
