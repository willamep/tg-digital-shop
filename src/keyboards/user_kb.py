from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardMarkup
from aiogram.filters.callback_data import CallbackData

class MainMenuCB(CallbackData, prefix="main"):
    page: str

# class catalogCB(CallbackData, prefix="cat"):
#     category_id: int

# class ItemCB(CallbackData, prefix="item"):
#     item_id: int

# class BuyCB(CallbackData, prefix="buy"):
#     page: int

# class ProfileCB(CallbackData, prefix="profile"):
#     user_id: int

# class CB(CallbackData, prefix=""):
#     page: int

def main_menu() -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for i in range(6):
        builder.button(text =f"Button {i}", callback_data=MainMenuCB(page=str(i)))
    builder.adjust(3, 2)
    return builder.as_markup()
