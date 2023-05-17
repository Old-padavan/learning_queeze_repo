from aiogram import Router
from aiogram.types import Message

router: Router = Router()

# Этот хэндлер будет реагировать на любые сообщения пользователя,
# не предусмотренные логикой работы бота
@router.message()
async def echo_message(message: Message):
    await message.answer(f'Извините, но я не понимаю команду {message.text}.'
                            'Пожалуйста, попробуйте еще раз или воспользуйтесь командой /help'
                            'для получения дополнительной информации о доступных командах')