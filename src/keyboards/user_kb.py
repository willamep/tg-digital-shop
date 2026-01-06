from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

class MainMenuCB(CallbackData, prefix="main"):
    chapter: str

# class catalogCB(CallbackData, prefix="cat"):
#     category_id: int

# class ItemCB(CallbackData, prefix="item"):
#     item_id: int

# class BuyCB(CallbackData, prefix="buy"):
#     chapter: int

# class ProfileCB(CallbackData, prefix="profile"):
#     user_id: int

# class CB(CallbackData, prefix=""):
#     chapter: int

def main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    builder.button(text=f"About Shop", callback_data=MainMenuCB(chapter="About Shop"))
    builder.button(text=f"My Orders", callback_data=MainMenuCB(chapter="My Orders"))
    builder.button(text=f"Catalog", callback_data=MainMenuCB(chapter="Catalog"))
    builder.adjust(2, 1)
    return builder.as_markup()
