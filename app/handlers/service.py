from aiogram.types import Message
from aiogram import Router, F

from keyboards.reply import get_keyboard
from handlers.commands import start_kb
from common.texts import telegram_text, service_text, tools_text
from common.kb_list import service_kb


service_router = Router()




@service_router.message(F.text == "💡Почему именно чат-боты в Telegram?")
async def echo(message: Message):
    await message.answer(telegram_text)
    
    
@service_router.message(F.text == "🛠Какие технологии вы используете?")
async def echo(message: Message):
    await message.answer(tools_text)
    
    
@service_router.message(F.text == "💻Мои услуги")
async def echo(message: Message):
    await message.answer(service_text, reply_markup=service_kb)
    
    
@service_router.message(F.text == "⬅️Назад к меню")
async def echo(message: Message):
    await message.answer("Вы вернулись в главное меню", reply_markup=start_kb)