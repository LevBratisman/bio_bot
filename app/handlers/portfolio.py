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
    await message.answer_photo(photo="AgACAgIAAxkBAAICFGYdJEj5TVZCtaldyJ5d2QJmIWF2AAIg2zEb5-XpSKpxvCPvbwTmAQADAgADcwADNAQ", 
                               caption=simple_ph_text)
    
@portfolio_router.message(F.text == "Бот для заказа пиццы")
async def echo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAICFmYdJFwNQJFs2l9pYF8lm65w3d1KAAIh2zEb5-XpSNVOOzAraqdFAQADAgADcwADNAQ", 
                               caption=roma_pizza_text)
    
@portfolio_router.message(F.text == "Кулинарный AI ассистент")
async def echo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAICGGYdJHIvJtca1S4kzi0aEu_5M_VHAAIi2zEb5-XpSHS27I1PsBKTAQADAgADcwADNAQ", 
                               caption=papion_text)
    
@portfolio_router.message(F.text == "Интернет-магазин одежды")
async def echo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAICCGYdI5RguYND3bV_LAjYaNtlDhxrAAJa2jEbEMToSL3E5BR5PBwyAQADAgADcwADNAQ", 
                               caption=clothy_text)
    
@portfolio_router.message(F.text == "Конвертер валют")
async def echo(message: Message):
    await message.answer_photo(photo="AgACAgIAAxkBAAICEmYdJDNTteA5y2MSZoRE4KXoXDocAAIf2zEb5-XpSLeeclptenHmAQADAgADcwADNAQ", 
                               caption=converter_text)