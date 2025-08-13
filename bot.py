from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler, MessageHandler, filters

# Вставь свой токен от @BotFather
BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Подати заявку", callback_data='apply')],
        [InlineKeyboardButton("Про компанію", callback_data='about')],
        [InlineKeyboardButton("FAQ", callback_data='faq')],
        [InlineKeyboardButton("Контакти", callback_data='contact')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привіт! Я HR-бот Velora Corp. Чим можу допомогти?", reply_markup=reply_markup
    )

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    if query.data == 'apply':
        await query.edit_message_text("Відправте своє резюме або короткий опис досвіду.")
    elif query.data == 'about':
        await query.edit_message_text("Velora Corp — простір для ідей та рішень. Наша місія: ...")
    elif query.data == 'faq':
        await query.edit_message_text("FAQ:\n1. Як подати заявку?\n2. Які умови співпраці?\n3. Як проходить відбір?")
    elif query.data == 'contact':
        await query.edit_message_text("📧 contact@veloracorp.com\n🌐 veloracorp.com")

async def receive_resume(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    # Здесь можно пересылать сообщение на email или в другой чат
    await update.message.reply_text(f"Дякуємо, {user.first_name}! Ми отримали вашу заявку.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button))
app.add_handler(MessageHandler(filters.Document.ALL | filters.TEXT, receive_resume))

app.run_polling()
