from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from main import dp
from ..utility.add_answer_form import add_answer_form


# создаем класс для хранения состояний
class AddAnswer(StatesGroup):
    """Хранит состояния процесса отправки ответа на задание"""
    waiting_for_first_name = State()
    waiting_for_last_name = State()
    waiting_for_answer = State()
    waiting_for_task_id = State()


# хэндлеры по заполнению полей формы отправки ответа
@dp.message_handler(commands='add_answer', state='*')
async def add_answer(message: types.Message):
    """В ответ на команду /add_answer переходит в состояние waiting_for_first_name и выводит сообщение о необходимости
       ввести имя"""
    await message.answer('Для отправки ответа на задание необходимо правильно заполнить все поля.')
    await AddAnswer.waiting_for_first_name.set()
    await message.answer('Введите имя:\n\n'
                         'Для отмены нажмите /cancel')


@dp.message_handler(state=AddAnswer.waiting_for_first_name)
async def add_answer_first_name(message: types.Message, state: FSMContext):
    """Ввод имени, сохранение и переход в следующее состояние"""
    await state.update_data(first_name=message.text)
    await AddAnswer.next()
    await message.answer('Введите фамилию:\n\n'
                         'Для отмены нажмите /cancel')


@dp.message_handler(state=AddAnswer.waiting_for_last_name)
async def add_answer_last_name(message: types.Message, state: FSMContext):
    """Ввод фамилии, сохранение и переход в следующее состояние"""
    await state.update_data(last_name=message.text)
    await AddAnswer.next()
    await message.answer('Введите ответ:\n\n'
                         'Для отмены нажмите /cancel')


@dp.message_handler(state=AddAnswer.waiting_for_answer)
async def add_answer_answer(message: types.Message, state: FSMContext):
    """Ввод ответа, сохранение и переход в следующее состояние"""
    await state.update_data(answer=message.text)
    await AddAnswer.next()
    await message.answer('Введите id задания:\n\n'
                         'Для отмены нажмите /cancel')


@dp.message_handler(state=AddAnswer.waiting_for_task_id)
async def add_answer_task_id(message: types.Message, state: FSMContext):
    """Ввод номера задания, сохранение, отправка формы и завершение состояния"""
    await state.update_data(task_id=message.text)
    user_data = await state.get_data()
    add_answer_form(user_data['first_name'], user_data['last_name'], user_data['answer'],
                    user_data['task_id'])
    await state.finish()
    await message.answer('Ответ отправлен!')
