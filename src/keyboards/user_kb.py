from aiogram.utils.keyboard         import InlineKeyboardBuilder
from aiogram.types                  import InlineKeyboardMarkup
from aiogram.filters.callback_data  import CallbackData

from database.db import get_categories, get_items

class MainMenuCB(CallbackData, prefix="main"):
    chapter: str

class CatalogCB(CallbackData, prefix="cat"):
    cat_id: int

class ItemCB(CallbackData, prefix="item"):
    item_id: int

# class BuyCB(CallbackData, prefix="buy"):
#     chapter: int

# class ProfileCB(CallbackData, prefix="profile"):
#     user_id: int

# class CB(CallbackData, prefix=""):
#     chapter: int

def main_menu_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=f"About Shop", callback_data=MainMenuCB(chapter="About Shop"))
    builder.button(text=f"My Orders",  callback_data=MainMenuCB(chapter="My Orders"))
    builder.button(text=f"Catalog",    callback_data=MainMenuCB(chapter="Catalog"))
    builder.adjust(2, 1)
    return builder.as_markup()

def about_shop_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=f"My Orders", callback_data=MainMenuCB(chapter="My Orders"))
    builder.button(text=f"Catalog",   callback_data=MainMenuCB(chapter="Catalog"))
    builder.adjust(2)
    return builder.as_markup()
    

def catalog_kb() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for cat in get_categories():
        builder.button(text=cat[1], callback_data=CatalogCB(cat_id=cat[0]))
    builder.button(text="Back", callback_data=MainMenuCB(chapter="Menu"))
    builder.adjust(2)
    return builder.as_markup()

def items_kb(cat_id) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for item in get_items(cat_id):
        builder.button(text=f"{item[1]} – {item[2]}", callback_data=ItemCB(item_id=item[0]))
    builder.button(text="Back", callback_data=MainMenuCB(chapter="Catalog"))
    builder.adjust(2)
    return builder.as_markup()
