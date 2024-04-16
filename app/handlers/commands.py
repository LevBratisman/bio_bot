from aiogram.filters import Command, CommandStart, StateFilter, or_f
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types.input_media_photo import InputMediaPhoto
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram import Router, F, Bot
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import asyncio

from sqlalchemy.ext.asyncio import AsyncSession


from common.texts import start_text, start_info_text, service_text, portfolio_text, about_text, feedback_text, price_text
from common.kb_list import start_kb, portfolio_kb, service_kb, cancel_kb
from database.dao import add_user


command_router = Router()


class SendFeedback(StatesGroup):
    feedback = State()
    
    
media = MediaGroupBuilder()
media.add_photo("AgACAgIAAxkBAAICHGYdJaqOAAH3a7zgKAwXYcnOTCckGgACstoxGxGE6UgE1F_O5hOqgAEAAwIAA3MAAzQE")
media.add_photo("AgACAgIAAxkBAAICwGYeF3JCrL_qjUsvtFO-nPh-pyLzAAL52zEbiEHxSJbW-TQ31OvBAQADAgADcwADNAQ")
media.add_photo("AgACAgIAAxkBAAICwmYeF3k_3qyyMNCbvQPTp8-WwROVAAL62zEbiEHxSMfqNiSGi1MVAQADAgADcwADNAQ")
media.add_photo("AgACAgIAAxkBAAICU2YdLPr2wb9nDa55ghLEAyRTd4rtAAJ-2zEb5-XpSO9kBtpv5b53AQADAgADcwADNAQ")


@command_router.message(CommandStart())
async def cmd_start(message: Message, session: AsyncSession):
    await message.answer(start_text)
    await asyncio.sleep(1.5)
    await message.answer(start_info_text, reply_markup=start_kb)
    await add_user(session, message.from_user.id, message.from_user.username)


@command_router.message(Command("about"))
async def cmd_about(message: Message):
    await message.answer(about_text)
    
    
@command_router.message(or_f(Command("price"), F.text == "💰Стоимость услуг"))
async def cmd_about(message: Message):
    await message.answer(price_text)
    
    
@command_router.message(Command("portfolio"))
async def cmd_portfolio(message: Message):
    await message.answer(portfolio_text, reply_markup=portfolio_kb)
    
    
@command_router.message(or_f(Command("request"), F.text == "📨Заказать бота"))
async def cmd_request(message: Message):
    await message.answer("По всем вопросам пишите @bratisman")


@command_router.message(or_f(Command("service"), F.text == "💻Мои услуги"))
async def cmd_service(message: Message, bot: Bot):
    await bot.send_media_group(message.chat.id, media.build())
    await message.answer(service_text, reply_markup=service_kb)
    
    
@command_router.message(or_f(Command("feedback"), F.text == "📝Оставить отзыв"))
async def cmd_feedback(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Оставить отзыв о проделанной работе вы можете по ссылке https://t.me/+sa--MXFoLpVhNzYy")
    await message.answer("❗️Отзывы, не относящиеся к моей работе, будут удалены.")

# FSM отправка отзыва -----------------------------------------

# @command_router.message(or_f(Command("feedback"), F.text == "📝Оставить отзыв"))
# async def cmd_feedback(message: Message, state: FSMContext):
#     await state.clear()
#     await state.set_state(SendFeedback.feedback)
#     await message.answer("✉️Напишите ваш отзыв", reply_markup=cancel_kb)
    
# @command_router.message(StateFilter(SendFeedback.feedback), F.text == "Отмена")
# async def cmd_feedback_cancel(message: Message, state: FSMContext):
#     await state.clear()
#     await message.answer("Вы вернулись в меню", reply_markup=start_kb)

# @command_router.message(StateFilter(SendFeedback.feedback), F.text)
# async def cmd_feedback_send(message: Message, state: FSMContext):
#     # user_id = await get_id_by_user_id(session, message.from_user.id)
#     # await add_review(session, user_id, message.text)
#     await state.clear()
#     await message.answer("Спасибо, отзыв был успешно отправлен!")
#     await message.answer("Вы вернулись в меню", reply_markup=start_kb)
    
    
# @command_router.message(StateFilter(SendFeedback.feedback))
# async def cmd_feedback_incorrect(message: Message, state: FSMContext):
#     await message.answer("Неверный формат данных")
    
    
# ---------------------------------------------------------------


