from aiogram.types.input_file import FSInputFile
from info import kb as info_kb
from aiogram import types
import requests


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

def get_mentors_info(direction: str):
    response = requests.post(
        'https://n8n.bauart.pro/webhook/0f63b965-3aac-4257-bd0f-bdfe8a9e15e0',
        json={
            'action': 'mentors',
            'payload': {
                'direction': direction,
            }
        },
    )
    message_text = ''
    for mentor in response.json():
        message_text += f'{mentor['name']}\n{mentor['property_description']}'

    return message_text

def check_auth(chat_id: int):
    response = requests.post(
        'https://n8n.bauart.pro/webhook/0f63b965-3aac-4257-bd0f-bdfe8a9e15e0',
        json={
            'action': 'check_autorize',
            'payload': {
                'chatId': chat_id,
            }
        },
    )
    if response.status_code == 200:
        return True
    else:
        return False
    
def auth(email: str, chat_id: int):
    response = requests.post(
        'https://n8n.bauart.pro/webhook/0f63b965-3aac-4257-bd0f-bdfe8a9e15e0',
        json={
            'action': 'register',
            'payload': {
                'email': email,
                'chatId': chat_id,
            }
        },
    )
    if response.status_code == 200:
        return True
    else:
        return False
    
def get_test_case(chat_id: int):
    response = requests.post(
        'https://n8n.bauart.pro/webhook/0f63b965-3aac-4257-bd0f-bdfe8a9e15e0',
        json={
            'action': 'test_task',
            'payload': {
                'chatId': chat_id,
            }
        },
    )
    return response.json()['task']


def send_test_case(github: str, chat_id: int):
    response = requests.post(
        'https://n8n.bauart.pro/webhook/0f63b965-3aac-4257-bd0f-bdfe8a9e15e0',
        json={
            'action': 'test_task_check',
            'payload': {
                'chatId': chat_id,
                'url': github,
            }
        },
    )
    if response.status_code == 200:
        return True
    else:
        return False