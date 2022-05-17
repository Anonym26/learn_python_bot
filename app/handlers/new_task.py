from aiogram import types

from app.utility.get_task_id import get_id_last_task
from main import dp


# обработчик команды /new_tasks
@dp.message_handler(commands=['new_task'])
async def new_task(message: types.Message):
    """Используя функцию get_id_last_task проверяет есть ли новые задания и выводит результат"""
    result = get_id_last_task()
    if result:
        await message.answer(f'Есть новое задание, под № {result}!')
    else:
        await message.answer('Новых заданий не появилось :(')
    await message.answer(f'Для перехода к заданиям нажмите https://imsr.su/')