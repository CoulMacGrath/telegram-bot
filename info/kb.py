from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    )


def create_inline_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Направления", callback_data='directions'),
            InlineKeyboardButton(text="Практика", callback_data='practice')
        ],
        [
            InlineKeyboardButton(text="Помощь", callback_data='help'),
            InlineKeyboardButton(text="Контакты", callback_data='contacts')
        ]
    ])
    return keyboard


def create_directions_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Backend", callback_data='backend'),
            InlineKeyboardButton(text="Frontend", callback_data='frontend'),
            InlineKeyboardButton(text="Fullstack", callback_data='fullstack'),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='back_start'),
        ],
    ])
    return keyboard


def create_practice_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Отчеты", callback_data='reports'),
            InlineKeyboardButton(text="Тестовые задания", callback_data='test_case'),
        ],
        [
            InlineKeyboardButton(text="Назад", callback_data='back_start'),
        ],
    ])
    return keyboard

def create_test_task_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Сдать тестовое", callback_data='send_test_task'),
            InlineKeyboardButton(text="Назад", callback_data='practice'),
        ],
    ])
    return keyboard

def create_back_start_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data='back_start'),
        ],
    ])
    return keyboard

def create_back_directions_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data='directions'),
        ],
    ])
    return keyboard

def create_back_practice_menu():
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="Назад", callback_data='practice'),
        ],
    ])
    return keyboard