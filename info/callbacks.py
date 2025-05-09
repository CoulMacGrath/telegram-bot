from aiogram import Router, types
from info import utils as info_utils
from aiogram.types.input_file import FSInputFile
from aiogram.types import InputMediaPhoto
from info import kb as info_kb


callbacks_router = Router()

@callbacks_router.callback_query(lambda cq: cq.data == "directions")
async def handle_more_info_callback(callback_query: types.CallbackQuery):
    keyboard = info_kb.create_directions_menu()
    await callback_query.message.edit_caption(caption="Направления",reply_markup=keyboard)
    await callback_query.answer("Информация по нарпавлениям", show_alert=False)

@callbacks_router.callback_query(lambda cq: cq.data == "practice")
async def handle_feedback_callback(callback_query: types.CallbackQuery):
    keyboard = info_kb.create_practice_menu()
    await callback_query.message.edit_caption(caption="Информация о практике", reply_markup=keyboard)
    await callback_query.answer("Информация о практике", show_alert=False)

@callbacks_router.callback_query(lambda cq: cq.data == "contacts")
async def handle_feedback_callback(callback_query: types.CallbackQuery):
    keyboard = info_kb.create_back_start_menu()
    await callback_query.message.edit_media(media=InputMediaPhoto(media=FSInputFile('./files/contacts.jpg')))
    await callback_query.message.edit_caption(
        caption=(
            "Есть вопросы?\n"
            "Свяжитесь с нами:\n"
            "📱 Мессенджеры: \n"
            "@Chichalov_Sergey \n"
            "@mr_tonik 89832044869 \n\n"
            "Наш сайт: https://bauart.pro/"
        ),
        reply_markup=keyboard,
    )
    await callback_query.answer("Контакты компании", show_alert=False)

@callbacks_router.callback_query(lambda cq: cq.data == "help")
async def handle_feedback_callback(callback_query: types.CallbackQuery):
    keyboard = info_kb.create_back_start_menu()
    await callback_query.message.edit_caption(caption="Какая-то помощь",reply_markup=keyboard)
    await callback_query.answer("Какая-то помощь", show_alert=False)

@callbacks_router.callback_query(lambda cq: cq.data == 'back_start')
async def back_to_start_handler(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await info_utils.send_welcome_message(callback_query.message)
    await callback_query.answer("Вернулся к началу", show_alert=False)