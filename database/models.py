from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase,relationship,mapped_column,Mapped,Session
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from config import MYSQL_URL

engine = create_async_engine(MYSQL_URL,echo=True)

async_session = async_sessionmaker(engine)


class Base(DeclarativeBase,AsyncAttrs):
    pass


class Category(Base):
    __tablename__ = 'categories'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    category_name: Mapped[str] = mapped_column(String(100))
    games = relationship('Game', back_populates='category')

class Game(Base):
    __tablename__ = 'games'

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    game_name: Mapped[str] = mapped_column(String(100))
    description: Mapped[str] = mapped_column(String(500))
    price: Mapped[int] = mapped_column(Integer)
    image: Mapped[str] = mapped_column(String(200))
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    category = relationship('Category',back_populates='games')

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


#Добавление игры
async def add_game():
    async with async_session() as session:
        # category = Category(category_name='Action')
        game = Game(game_name='Call of Duty: Infinite Warfare',
                    description='Прикольная игра чо',
                    price =7,
                    image='database\images\CoD_Infinite_Warfare.jpg',
                    category_id=3)
        session.add(game)
        await session.commit()
        await session.refresh(game)
        return game


