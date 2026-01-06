# Imports from aiogram
from aiogram import Router, F, html
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

# Imports from project files
from keyboards import MainMenuCB, main_menu # , catalog_kb
# from services.product import get_products
# from database.db import add_order

# Creating the router
router = Router()

# Handler for the /start command
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"{start_text(message.from_user.full_name)}",
        reply_markup=main_menu()
    )

@router.message()
async def unknown_command(message: Message) -> None:
    await message.answer(
        "What language is this? I don't understand. Let's speak at basic.\n\n"
        f"{start_text(message.from_user.full_name)}",
        reply_markup=main_menu()
    ) 

@router.callback_query(MainMenuCB.filter(F.chapter == "Catalog"))
async def catalog(query: CallbackQuery, callback_data: MainMenuCB):
    await query.answer()
    await query.message.edit_text("Catalog")

@router.callback_query(MainMenuCB.filter(F.chapter == "My Orders"))
async def catalog(query: CallbackQuery, callback_data: MainMenuCB):
    await query.answer()
    await query.message.edit_text("Info about orders")

@router.callback_query(MainMenuCB.filter(F.chapter == "About Shop"))
async def catalog(query: CallbackQuery, callback_data: MainMenuCB):
    await query.answer()
    await query.message.edit_text("Info about shop")

def start_text(full_name: str) -> str:
    return (
        f"Hello, {html.bold(full_name)}!\n"
        "In this bot you can buy goods from a universe far, far away."
    )
