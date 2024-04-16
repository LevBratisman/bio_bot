from datetime import date
from sqlalchemy import String, Date, func, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    created: Mapped[date] = mapped_column(Date, default=func.current_date())
    updated: Mapped[date] = mapped_column(Date, default=func.current_date(), onupdate=func.current_date())
    
    
class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(unique=True)
    user_name: Mapped[str] = mapped_column(String(150), nullable=True)
    
    
class Event(Base):
    __tablename__ = 'event'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column()