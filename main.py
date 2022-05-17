import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand
from aiogram.utils import executor

from config import BOT_TOKEN, admin_id

# Объект бота
bot = Bot(BOT_TOKEN, parse_mode="HTML")

# Диспетчер для бота
loop = asyncio.get_event_loop()
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage, loop=loop)

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)


async def send_to_admin(dp):
    await bot.send_message(chat_id=admin_id, text=f"bot_started")
    await set_commands(dp)


async def set_commands(dp):
    """Отображает меню с командами"""
    commands = [
        BotCommand(command="/new_task", description="Проверить новое задание"),
        BotCommand(command="/get_task", description="Получить текст задания"),
        BotCommand(command="/add_task", description="Добавить новое задание"),
        BotCommand(command="/add_answer", description="Добавить ответ"),
        BotCommand(command="/cancel", description="Отменить текущее действие")
    ]
    await bot.set_my_commands(commands)


if __name__ == '__main__':
    # Запуск бота
    from app.handlers import dp
    executor.start_polling(dp, on_startup=send_to_admin, skip_updates=True)
