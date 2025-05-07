from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    )

def create_reply_main_menu():
    keyboard = ReplyKeyboardMarkup(keyboard=[
        [
            KeyboardButton(text="Направления"),
            KeyboardButton(text="Практика")
        ],
    ], resize_keyboard=True)
    return keyboard

def create_inline_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Направления", callback_data="more_info"),
            InlineKeyboardButton(text="Практика", callback_data="feedback")
        ],
    ])
    return keyboard