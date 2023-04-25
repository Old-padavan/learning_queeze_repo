from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove, Message)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

API_TOKEN: str = '6030785391:AAFiapS-QAvi1-FAR2tx0o5YEl9WtxtqUGo'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Инициализируем объект билдера
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем список с кнопками
buttons_1: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 1}') for i in range(10)]

# Распаковываем второй список с кнопками методом add
kb_builder.add(*buttons_1)

# Явно сообщаем билдеру сколько хотим видеть кнопок в 1-м и 2-м рядах,
# а также говорим методу повторять такое размещение для остальных рядов
kb_builder.adjust(2, 1, repeat=True)

# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_command_start(message: Message):
# Методом as_markup() передаем клавиатуру как аргумент туда, где она требуется
    await message.answer(text='Вот такая получается клавиатура', reply_markup=kb_builder.as_markup(
        resize_keyboard=True))

if __name__ == '__main__':
    dp.run_polling(bot)
