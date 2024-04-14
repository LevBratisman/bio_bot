from aiogram.types import Message
from aiogram import Router, F

from keyboards.reply import get_keyboard

from common.texts import portfolio_text, about_text, roma_pizza_text, converter_text, papion_text, clothy_text, simple_ph_text
from common.kb_list import portfolio_kb, start_kb


portfolio_router = Router()



@portfolio_router.message(F.text == "⬅️Назад к меню")
async def echo(message: Message):
    await message.answer("Вы вернулись в меню", reply_markup=start_kb)
    
@portfolio_router.message(F.text == "🤖Мои работы")
async def get_portfolio(message: Message):
    await message.answer(portfolio_text, reply_markup=portfolio_kb)
    
@portfolio_router.message(F.text == "Бот-справочник по физике")
async def echo(message: Message):
    await message.answer(simple_ph_text)
    
@portfolio_router.message(F.text == "Бот для заказа пиццы")
async def echo(message: Message):
    await message.answer(roma_pizza_text)
    
@portfolio_router.message(F.text == "Кулинарный AI ассистент")
async def echo(message: Message):
    await message.answer(papion_text)
    
@portfolio_router.message(F.text == "Интернет-магазин одежды")
async def echo(message: Message):
    await message.answer(clothy_text)
    
@portfolio_router.message(F.text == "Конвертер валют")
async def echo(message: Message):
    await message.answer(converter_text)