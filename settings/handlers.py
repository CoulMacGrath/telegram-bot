from aiogram import Router

# Импортируем роутеры отдельных модулей
from info.handlers import info_router
# Аналогично поступаем с остальными роутерами
# from reports.handlers import report_router
# from test_tasks.handlers import test_tasks_router

main_router = Router()

# Добавляем роутеры
main_router.include_router(info_router)
# main_router.include_router(report_router)
# main_router.include_router(test_tasks_router)