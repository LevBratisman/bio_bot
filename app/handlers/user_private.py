from aiogram.types import Message
from aiogram import Router, F

from common.texts import about_text


user_private_router = Router()

@user_private_router.message(F.text == "🙋🏻‍♂️Информация обо мне")
async def get_info(message: Message):
    await message.answer(about_text)
    
    
@user_private_router.message(F.photo)
async def get_info(message: Message):
    await message.answer(message.photo[0].file_id)