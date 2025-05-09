from aiogram import Router, types
from info import utils as info_utils
from aiogram.types.input_file import FSInputFile
from aiogram.types import InputMediaPhoto,Message
from info import kb as info_kb
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State


callbacks_router = Router()

@callbacks_router.callback_query(lambda cq: cq.data == 'directions')
async def handle_more_info_callback(callback_query: types.CallbackQuery):
    keyboard = info_kb.create_directions_menu()
    await callback_query.message.edit_media(media=InputMediaPhoto(media=FSInputFile('./files/directions.jpg')))
    await callback_query.message.edit_caption(caption='Направления',reply_markup=keyboard)
    await callback_query.answer('Информация по нарпавлениям', show_alert=False)

@callbacks_router.callback_query(lambda cq: cq.data == 'practice')
async def handle_feedback_callback(callback_query: types.CallbackQuery):
    keyboard = info_kb.create_practice_menu()
    await callback_query.message.edit_media(media=InputMediaPhoto(media=FSInputFile('./files/practice.jpg')))
    await callback_query.message.edit_caption(caption='Информация о практике', reply_markup=keyboard)
    await callback_query.answer('Информация о практике', show_alert=False)

@callbacks_router.callback_query(lambda cq: cq.data == 'contacts')
async def handle_feedback_callback(callback_query: types.CallbackQuery):
    keyboard = info_kb.create_back_start_menu()
    await callback_query.message.edit_media(media=InputMediaPhoto(media=FSInputFile('./files/contacts.jpg')))
    await callback_query.message.edit_caption(
        caption=(
            'Есть вопросы?\n'
            'Свяжитесь с нами:\n'
            '📱 Мессенджеры: \n'
            '@Chichalov_Sergey \n'
            '@mr_tonik 89832044869 \n\n'
            'Наш сайт: https://bauart.pro/'
        ),
        reply_markup=keyboard,
    )
    await callback_query.answer('Контакты компании', show_alert=False)


@callbacks_router.callback_query(lambda cq: cq.data == 'test_case')
async def handle_test_case(callback_query: types.CallbackQuery):
    test_case = info_utils.get_test_case(callback_query.message.chat.id)
    keyboard = info_kb.create_test_task_menu()
    await callback_query.message.edit_caption(caption=test_case, reply_markup=keyboard,)
    await callback_query.answer('Вот твое тестовое задание!', show_alert=False)

class GitHubForm(StatesGroup):
    GIT_HUB_INPUT = State()

@callbacks_router.callback_query(lambda cq: cq.data == 'send_test_task')
async def handle_send_test_task(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.message.answer("Введите сслыку на github репозиторий с вашим тестовым заданием:")
    await state.set_state(GitHubForm.GIT_HUB_INPUT)


@callbacks_router.message(GitHubForm.GIT_HUB_INPUT)
async def submit_email(msg: Message, state: FSMContext):
    inline_keyboard = info_kb.create_back_practice_menu()
    github = msg.text.strip()
    test_case = info_utils.send_test_case(github, msg.chat.id)
    if test_case: 
        await msg.answer_photo(
            photo=FSInputFile('./files/practice.jpg'),
            caption='Вы отправили задание на проверку',
            reply_markup=inline_keyboard
        )
    else:
        await msg.answer_photo(
            photo=FSInputFile('./files/practice.jpg'),
            caption='Вы уже сдали задание',
            reply_markup=inline_keyboard
        )


@callbacks_router.callback_query(lambda cq: cq.data == 'help')
async def handle_feedback_callback(callback_query: types.CallbackQuery):
    keyboard = info_kb.create_back_start_menu()
    await callback_query.message.edit_caption(caption='Какая-то помощь',reply_markup=keyboard)
    await callback_query.answer('Какая-то помощь', show_alert=False)

@callbacks_router.callback_query(lambda cq: cq.data == 'back_start')
async def back_to_start_handler(callback_query: types.CallbackQuery):
    await callback_query.message.delete()
    await info_utils.send_welcome_message(callback_query.message)
    await callback_query.answer('Вернулся к началу', show_alert=False)


@callbacks_router.callback_query(lambda cq: cq.data == 'backend')
async def handle_more_info_callback(callback_query: types.CallbackQuery):
    keyboard = info_kb.create_back_directions_menu()
    message_text = info_utils.get_mentors_info('Backend')
    await callback_query.message.edit_media(media=InputMediaPhoto(media=FSInputFile('./files/contacts.jpg')))
    await callback_query.message.edit_caption(caption=message_text,reply_markup=keyboard)
    await callback_query.answer('Информация по нарпавлениям', show_alert=False, parse_mode='MarkdownV2')

@callbacks_router.callback_query(lambda cq: cq.data == 'frontend')
async def handle_more_info_callback(callback_query: types.CallbackQuery):
    keyboard = info_kb.create_back_directions_menu()
    message_text =  info_utils.get_mentors_info('Frontend')
    await callback_query.message.edit_media(media=InputMediaPhoto(media=FSInputFile('./files/contacts.jpg')))
    await callback_query.message.edit_caption(caption=message_text,reply_markup=keyboard)
    await callback_query.answer('Информация по нарпавлениям', show_alert=False, parse_mode='MarkdownV2')

@callbacks_router.callback_query(lambda cq: cq.data == 'fullstack')
async def handle_more_info_callback(callback_query: types.CallbackQuery):
    keyboard = info_kb.create_back_directions_menu()
    message_text = info_utils.get_mentors_info('Fullstack')
    await callback_query.message.edit_media(media=InputMediaPhoto(media=FSInputFile('./files/contacts.jpg')))
    await callback_query.message.edit_caption(caption=message_text,reply_markup=keyboard)
    await callback_query.answer('Информация по нарпавлениям', show_alert=False, parse_mode='MarkdownV2')
