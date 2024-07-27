from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,ReplyKeyboardMarkup,KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder,ReplyKeyboardBuilder
from database.requests import *

kb = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Категории')],
    [KeyboardButton(text='Игры')],
    [KeyboardButton(text='Помощь')]
],resize_keyboard=True,input_field_placeholder='Выберите кнопку',
one_time_keyboard=True)

# kb1 = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Scrap Mechanic',callback_data='scrap mechanic')],
#     [InlineKeyboardButton(text='Minecraft',callback_data='Minecraft')],
#     [InlineKeyboardButton(text='RDR2',callback_data='RDR2')]
# ])

# kb2 = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Онлайн игра',callback_data='Online')],
#     [InlineKeyboardButton(text='Одиночная игра',callback_data='Solo')],
#     [InlineKeyboardButton(text='Кооператив',callback_data='coop')],
# ])

# async def builder_kb():
#     num = ReplyKeyboardBuilder()
#     for i in range(1, 17):
#         num.add(KeyboardButton(text=str(i)))
#     return num.adjust(4).as_markup()


async def categories():
    category_kb = InlineKeyboardBuilder()
    categories = await get_category()
    for category in categories:
        category_kb.add(InlineKeyboardButton(
            text=category.category_name,
            callback_data=f'category_{category.id}'
        ))
    return category_kb.adjust(2).as_markup()

async def categorier():
    category_kb = InlineKeyboardBuilder()
    categories = await get_category()
    for category in categories:
        category_kb.add(InlineKeyboardButton(
            text=category.category_name,
            callback_data=f'categoryer_{category.id}'
        ))
    return category_kb.adjust(2).as_markup()

# async def games():
#     games_kb = InlineKeyboardBuilder()
#     all_games = await get_games()
#     for game in all_games:
#         games_kb.add(InlineKeyboardButton(
#             text=game.game_name,
#             callback_data=f'game_{game.id}'
#         ))
#     return games_kb.adjust(2).as_markup()
PAGE_SIZE = 2
async def games(category_id, page):
    offset = (page - 1) * PAGE_SIZE
    games_kb = InlineKeyboardBuilder()
    all_games = await get_games_cat(category_id=category_id, offset=offset, limit=PAGE_SIZE)
    
    for game in all_games:
        games_kb.add(InlineKeyboardButton(
            text=game.game_name,
            callback_data=f'game_{game.id}'
        ))

    # Add navigation buttons
    if page > 1:
        games_kb.add(InlineKeyboardButton(
            text='<--',
            callback_data=f'page_{category_id}_{page-1}'
        ))
    if len(all_games) == PAGE_SIZE:
        games_kb.add(InlineKeyboardButton(
            text='-->',
            callback_data=f'page_{category_id}_{page+1}'
        ))
    
    return games_kb.adjust(2).as_markup()

async def games_category(category_id):
    game_kb = InlineKeyboardBuilder()
    games_cat = await get_games_cat(category_id)
    for game_cat in games_cat:
        game_kb.add(InlineKeyboardButton(
            text=game_cat.game_name,
            callback_data=f'game_{game_cat.id}'))
    return game_kb.adjust(2).as_markup()

async def back():
    back_kb = InlineKeyboardBuilder()
    back_kb.add(InlineKeyboardButton(
        text='Назад',
        callback_data='back_to_categories'))
    return back_kb.as_markup()

async def back_delete(game_id):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Назад', callback_data=f'back_to_categories')],
        [InlineKeyboardButton(text='Удалить', callback_data=f'delete_{game_id}')]
    ])
    return kb
