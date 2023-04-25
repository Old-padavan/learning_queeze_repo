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

# Создаем первый список с кнопками
buttons_1: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 1}') for i in range(5)]

## Создаем второй список с кнопками
buttons_2: list[KeyboardButton] = [KeyboardButton(text=f'Кнопка {i + 6}') for i in range(10)]

# Распаковываем список с кнопками в билдер методом row,
# указываем, что в одном ряду должно быть 4 кнопки
kb_builder.row(*buttons_1, width=4)

# Распаковываем второй список с кнопками методом add
kb_builder.add(*buttons_2)

# Этот хэндлер будет срабатывать на команду "/start"
# и отправлять в чат клавиатуру
@dp.message(CommandStart())
async def process_command_start(message: Message):
# Методом as_markup() передаем клавиатуру как аргумент туда, где она требуется
    await message.answer(text='Вот такая получается клавиатура', reply_markup=kb_builder.as_markup(
        resize_keyboard=True))

if __name__ == '__main__':
    dp.run_polling(bot)
