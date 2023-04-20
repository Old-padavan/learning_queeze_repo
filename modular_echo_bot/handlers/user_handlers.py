from aiogram.types import Message
from aiogram.filters import Command, CommandStart
from create_dp import dp
from lexicon.lexicon import LEXICON_RU

@dp.message(CommandStart())
async def command_start_process(message: Message):
    await message.answer(text=LEXICON_RU['/start'])

# Этот хэндлер срабатывает на команду /help
@dp.message(Command(commands='help'))
async def command_help_process(message: Message):
    await message.answer(text=LEXICON_RU['/help'])
