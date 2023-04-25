from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder

API_TOKEN: str = '6030785391:AAFiapS-QAvi1-FAR2tx0o5YEl9WtxtqUGo'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

# Инициализируем билдер
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем кнопки
contact_btn: KeyboardButton = KeyboardButton(text='Отправить телефон', requst_contact=True)
geo_btn: KeyboardButton = KeyboardButton(text='Отправить геопозицию', request_location=True)
poll_btn: KeyboardButton = KeyboardButton(text='Создать викторину или опрос',
                                          request_poll=KeyboardButtonPollType())

# Добавляем кнопки в билдер
kb_builder.row(contact_btn, geo_btn, poll_btn)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(resize_keyboard=True, one_time_keyboard=True)

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Эксперементируем со специальными кнопками', reply_markup=keyboard)

if __name__ == '__main__':
    dp.run_polling(bot)
