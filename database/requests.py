from database.models import Category,Game,async_session


from sqlalchemy import select, delete, update 


async def get_category():
    async with async_session() as session:
        result = await session.scalars(select(Category))
        return result
    
async def get_games():
    async with async_session() as session:
        result_game = await session.scalars(select(Game))
        return result_game
    
# async def get_games_cat(category_id):
#     async with async_session() as session:
#         result_cat_id = await session.scalars(
#             select(Game).where(Game.category_id == category_id))
#         return result_cat_id
    

async def get_games_cat(category_id, offset, limit):
    async with async_session() as session:
        result_cat_id = await session.scalars(
            select(Game).where(Game.category_id == category_id).offset(offset).limit(limit)
        )
        return result_cat_id.all()
    
async def get_game_info(game_id):
    async with async_session() as session:
        result_game_id = await session.scalar(
            select(Game).where(Game.id == game_id))
        return result_game_id
    
async def add_category_to_db(category):
    async with async_session() as session:
        session.add(category)
        await session.commit()
        await session.refresh(category)
        return category
    
async def add_igra(game):
    async with async_session() as session:
        session.add(game)
        await session.commit()
        await session.refresh(game)
        return game
    
async def delete_game_request(game_id):
    async with async_session() as session:
        await session.execute(
            delete(Game).where(Game.id == game_id))
        await session.commit()