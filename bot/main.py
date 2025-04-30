import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from settings.config import settings

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Меню с кнопками
MENU_KEYBOARD = ReplyKeyboardMarkup([
    [KeyboardButton("Сдай задание"), KeyboardButton("Запишись на собес")],
    [KeyboardButton("Кто менторы"), KeyboardButton("Какие направления")]
], resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Команда /start."""
    await update.message.reply_text("Выберите интересующее вас действие:", reply_markup=MENU_KEYBOARD)

async def menu_choice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обрабатывает выбор пользователя из меню."""
    choice = update.message.text
    match choice:
        case "Сдай задание":
            await update.message.reply_text("Отправьте своё задание для сдачи.")
        case "Запишись на собес":
            await update.message.reply_text("Оставьте заявку на собеседование.")
        case "Кто менторы":
            await update.message.reply_text("Наши ментора:\nИван Иванов\nМарья Петрова")
        case "Какие направления":
            await update.message.reply_text("Доступные направления:\nFrontend\nBackend\nQA")
        case _:
            await update.message.reply_text("Неверный выбор. Выберите один из вариантов меню.")

def main() -> None:
    application = ApplicationBuilder().token(settings.TELEGRAM_BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), menu_choice))

    logger.info("Telegram-бот запущен...")
    application.run_polling()

if __name__ == '__main__':
    main()