import datetime
from sqlalchemy import delete, func, select
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import User, Event
from database.init import create_db


# ---------------------------------- USER DAO ------------------------------------

# Добавление пользователя
async def add_user(
    session: AsyncSession,
    user_id: int,
    user_name: str | None = None,
):
    query = select(User).where(User.user_id == user_id)
    result = await session.execute(query)
    
    if result.first() is None:
        session.add(User(user_id=user_id, 
                         user_name=user_name))
        await session.commit()
        

# Получение всех пользователей
async def get_all_users_id(session: AsyncSession):
    query = select(User.user_id)
    result = await session.execute(query)
    return result.scalars().all()


# Получение id пользователя по user_id
async def get_id_by_user_id(session: AsyncSession, user_id: int):
    query = select(User.id).where(User.user_id == user_id)
    result = await session.execute(query)
    return result.scalars().first()


async def get_count_users_last_days(session: AsyncSession, days: int):
    query = select(User.id).where(User.created >= (datetime.datetime.now() - datetime.timedelta(days=days)))
    result = await session.execute(query)
    return result.scalars().all()
    
    
# ---------------------------------- EVENT DAO ------------------------------------
    
    
async def add_event(session: AsyncSession, user_id: int):
    session.add(Event(user_id=user_id))
    await session.commit()
    
    
async def get_count_events_by_day(session: AsyncSession):
    query = select(Event.id).where(Event.created >= (datetime.datetime.now() - datetime.timedelta(days=1)))
    result = await session.execute(query)
    return result.scalars().all()


async def get_avarage_count_events_by_users(session: AsyncSession):
    query = select(func.count(Event.id)).group_by(Event.user_id)
    result = await session.execute(query)
    return result.scalars().all()


async def clear_event(session: AsyncSession):
    query = delete(Event)
    await session.execute(query)
    await session.commit()
    await create_db()