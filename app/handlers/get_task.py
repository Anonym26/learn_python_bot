from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from app.utility.get_task_for_id import search_task_for_id
from main import dp


# создаем класс для хранения состояний
class GetTask(StatesGroup):
    number_task = State()


# обработчик команды /get_task
@dp.message_handler(commands=['get_task'])
async def get_task(message: types.Message, state: FSMContext):
    """В ответ на команду /get_task переходит в состояние number_task и выводит сообщение о необходимости
        ввести номер задания"""
    await GetTask.number_task.set()
    await message.answer('Введите номер задания:\n\n'
                         f'Для отмены нажмите /cancel')


@dp.message_handler(state=GetTask.number_task)
async def number_task(message: types.Message, state: FSMContext):
    """Используя функцию get_id_last_task выводит текст запрашиваемого задания, после проверок"""
    await state.update_data(number_task=message.text)
    if not message.text.isdigit():
        await message.answer('Введено неверное значение!\n'
                             f'Введите номер задания:\n\n'
                             f'Для отмены нажмите /cancel')
        return
    user_data = await state.get_data()
    result = search_task_for_id(user_data['number_task'])
    if not result:
        await message.answer(f'Задание не найдено!\n'
                             f'Введите номер задания:\n\n'
                             f'Для отмены нажмите /cancel')
        return
    await message.answer(result)
    await state.finish()
