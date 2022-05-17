from aiogram import types
from aiogram.dispatcher import FSMContext

from main import dp


# обработчик команды /cancel
@dp.message_handler(commands='cancel', state='*')
async def cmd_cancel(message: types.Message, state: FSMContext):
    """Отменяет текущее действие (завершает состояние)"""
    await state.finish()
    await message.answer('Действие отменено')

