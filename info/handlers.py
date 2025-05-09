from aiogram.types import Message,FSInputFile
from aiogram.filters import Command
from aiogram import Router, types
from info import kb as info_kb
from info.callbacks import callbacks_router
from info import utils as info_utils
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

info_router = Router(name="info-handlers")
info_router.include_router(callbacks_router)


class LoginForm(StatesGroup):
    EMAIL_INPUT = State()

@info_router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext):
    auth = info_utils.check_auth(msg.chat.id)
    if auth:
        await info_utils.send_welcome_message(msg)
    else:
        await msg.answer("Введите ваш email для авторизации:")
        await state.set_state(LoginForm.EMAIL_INPUT)


@info_router.message(LoginForm.EMAIL_INPUT)
async def submit_email(msg: Message, state: FSMContext):
    email = msg.text.strip()
    auth = info_utils.auth(email, msg.chat.id)
    if auth: 
        await info_utils.send_welcome_message(msg)
    else:
        await msg.answer(f"Ошибка при регистрации, проверьте email, или обратитесь за помощью")

__all__ = ["info_router"] 