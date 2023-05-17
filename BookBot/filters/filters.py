from aiogram.filters import BaseFilter
from aiogram.types import CallbackQuery

# Проверяем callback_data у объекта CallbackQuery на то, что он состоит из цифр
class IsDigitCallbackData(BaseFilter):
    async def __call__(self, callback:CallbackQuery) -> bool:
        return isinstance(callback.data, str) and callback.data.isdigit()

# Ловим callback_data от кнопок-закладок, которые нужно удалить в режиме редактирования закладок
class IsDelBookmarkCallbackData(BaseFilter):
    async def __call__(self, callback: CallbackQuery) -> bool:
        return isinstance(callback.data, str) and 'del' in callback.data \
            and callback.data[:-3].isdigit()
