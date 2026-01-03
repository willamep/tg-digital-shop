# Imports from aiogram
from aiogram import Router, F, html
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

# Imports from project files
# from keyboards.user_kb import main_menu, catalog_kb
# from services.product import get_products
# from database.db import add_order

# Creating the router
router = Router()

# Handler for the /start command
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"Hello, {html.bold(message.from_user.full_name)}!\n"
        f"In this bot You can buy goods from a universe far, far away."
    )

@router.message()
async def unknown_command(message: Message) -> None:
    await message.answer("What language is this? I don't understand.")