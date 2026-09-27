
import os
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Konfigurimi i logimit
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Funksioni per komanden /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"Përshëndetje {user_name}! Mirë se erdhe te boti ynë. "
        "Ky bot funksionon 24/7 për të menaxhuar kanalin dhe pagesat."
    )

if __name__ == '__main__':
    # Vendos Token-in e BotFather ketu ose ne Environment Variables
    TOKEN = "VENDOS_TOKEN_E_BOT_FATHER_KETU"
    
    application = ApplicationBuilder().token(TOKEN).build()
    
    # Shto komandën /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    print("Boti po niset...")
    application.run_polling()
