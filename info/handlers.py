from aiogram.types import Message,FSInputFile
from aiogram.filters import Command
from aiogram import Router, types
from info import kb as info_kb

info_router = Router(name="info-handlers")


@info_router.message(Command("start"))
async def start_handler(msg: Message):
    reply_keyboard = info_kb.create_reply_main_menu()
    inline_keyboard = info_kb.create_inline_menu()
    welcome_message = (
        "🎓 Привет, студент!\n\n"
        "Добро пожаловать в нашего помощника по практике!\n"
        "Я помогу тебе разобраться с задачами, сроками, отчётами и всем, что связано с прохождением практики.\n\n"
        "📌 Готов начать? Просто напиши /start или выбери нужный раздел из меню.\n\n"
        "Если появятся вопросы — не стесняйся обращаться! 💬"
    )

    await msg.answer_photo(
            photo=FSInputFile('./files/start.png'),
            caption=welcome_message,
            reply_markup=inline_keyboard
        )

    await msg.answer(" ", reply_markup=reply_keyboard)

__all__ = ["info_router"] 