from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from  sqlalchemy.orm import  DeclarativeBase, sessionmaker
from app.config import settings






engine = create_async_engine(settings.DATABASE_URL)


async_session_maker = async_sessionmaker(
    bind=engine,           # Передаем наш асинхронный движок
    class_=AsyncSession,   # Явно указываем класс сессии
    expire_on_commit=False # Для асинхронности лучше ставить False
)

class Base(DeclarativeBase):
    pass