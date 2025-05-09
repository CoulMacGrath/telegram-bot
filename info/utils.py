from aiogram.types.input_file import FSInputFile
from info import kb as info_kb
from aiogram import types


async def send_welcome_message(message: types.Message):
    inline_keyboard = info_kb.create_inline_menu()
    welcome_message = (
        "🎓 Привет, студент!\n\n"
        "Добро пожаловать в нашего помощника по практике!\n"
        "Я помогу тебе разобраться с задачами, сроками, отчётами и всем, что связано с прохождением практики.\n\n"
        "📌 Готов начать? Просто напиши /start или выбери нужный раздел из меню.\n\n"
        "Если появятся вопросы — не стесняйся обращаться! 💬"
    )

    await message.answer_photo(
        photo=FSInputFile('./files/start.png'),
        caption=welcome_message,
        reply_markup=inline_keyboard
    )