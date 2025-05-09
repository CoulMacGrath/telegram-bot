from aiogram.types import Message,FSInputFile
from aiogram.filters import Command
from aiogram import Router, types
from info import kb as info_kb
from info.callbacks import callbacks_router
from info import utils as info_utils


info_router = Router(name="info-handlers")
info_router.include_router(callbacks_router)


@info_router.message(Command("start"))
async def start_handler(msg: Message):
    await info_utils.send_welcome_message(msg)

__all__ = ["info_router"] 