import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from settings.config import settings

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Я Telegram-бот.')

def main() -> None:
    application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    
    application.run_polling()

if __name__ == '__main__':
    main()