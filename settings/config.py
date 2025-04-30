from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Класс настроек для Telegram-бота.
    Все настройки автоматически загружаются из переменных окружения или файла .env.
    """
    TELEGRAM_BOT_TOKEN: str

    class Config:
        case_sensitive = True
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()