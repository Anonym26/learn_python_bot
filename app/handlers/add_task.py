from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from main import dp
from ..utility.add_task_form import add_task_form


# создаем класс для хранения состояний
class AddTask(StatesGroup):
    """Хранит состояния процесса отправки задания"""
    title = State()
    description = State()
    start_code = State()
    comment = State()


# хэндлеры по заполнению полей формы отправки ответа
@dp.message_handler(commands='add_task', state='*')
async def add_task(message: types.Message):
    """В ответ на команду /add_task переходит в состояние title и выводит сообщение о необходимости
    ввести заголовок задания"""
    await message.answer('Для отправки задания необходимо правильно заполнить все поля.')
    await AddTask.title.set()
    await message.answer('Введите заголовок задания:\n\n'
                         'Для отмены нажмите /cancel')


@dp.message_handler(state=AddTask.title)
async def add_title(message: types.Message, state: FSMContext):
    """Ввод заголовка задания, сохранения и переход в следующее состояние"""
    await state.update_data(title=message.text)
    await AddTask.next()
    await message.answer('Введите задание:\n\n'
                         'Для отмены нажмите /cancel')


@dp.message_handler(state=AddTask.description)
async def add_description(message: types.Message, state: FSMContext):
    """Ввод текста задания, сохранения и переход в следующее состояние"""
    await state.update_data(description=message.text)
    await AddTask.next()
    await message.answer('Введите задание:\n\n'
                         'Для отмены нажмите /cancel')


@dp.message_handler(state=AddTask.start_code)
async def add_start_code(message: types.Message, state: FSMContext):
    """Ввод начального кода задания, сохранения и переход в следующее состояние"""
    await state.update_data(start_code=message.text)
    await AddTask.next()
    await message.answer('Введите начальный код:\n\n'
                         'Для отмены нажмите /cancel')


@dp.message_handler(state=AddTask.comment)
async def add_comment(message: types.Message, state: FSMContext):
    """Ввод комментария к заданию, сохранения, отправки формы и завершение состояния"""
    await state.update_data(comment=message.text)
    user_data = await state.get_data()
    add_task_form(user_data['title'], user_data['description'], user_data['start_code'],
                  user_data['comment'])
    await state.finish()
    await message.answer('Задание отправлено!')
