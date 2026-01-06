# Imports from aiogram
from aiogram            import Router, F, html
from aiogram.filters    import Command, CommandStart
from aiogram.types      import Message, CallbackQuery

# Imports from project files
from keyboards import MainMenuCB, main_menu_kb, CatalogCB, catalog_kb, about_shop_kb, ItemCB, items_kb
# from services.product import get_products
# from database.db import add_order

# Creating the router
router = Router()

# Handler for the /start command
@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(
        f"{start_text(message.from_user.full_name)}",
        reply_markup=main_menu_kb()
    )

@router.message()
async def unknown_command(message: Message) -> None:
    await message.answer(
        "What language is this? I don't understand. Let's speak at basic.\n\n"
        f"{start_text(message.from_user.full_name)}",
        reply_markup=main_menu_kb()
    ) 

# Main menu callback handlers
@router.callback_query(MainMenuCB.filter(F.chapter == "Catalog"))
async def catalog(query: CallbackQuery, callback_data: MainMenuCB):
    await query.answer()
    await query.message.edit_text("Select a category", reply_markup=catalog_kb())

@router.callback_query(MainMenuCB.filter(F.chapter == "My Orders"))
async def orders(query: CallbackQuery, callback_data: MainMenuCB):
    await query.answer()
    await query.message.edit_text("Info about orders")

@router.callback_query(MainMenuCB.filter(F.chapter == "About Shop"))
async def about_shop(query: CallbackQuery, callback_data: MainMenuCB):
    await query.answer()
    text = '''The Mandalorian's shop delivers goods from all over the universe, regardless of rarity: lightsabers, portal guns, globetrotters, fighter jets, and much, much more!\n(it's all a joke and a pet-project)\n\n
    Bot Creator: @Avocatocat'''
    await query.message.edit_text(text, reply_markup=about_shop_kb())

# Catalog handler
@router.callback_query(CatalogCB.filter())
async def items(query: CallbackQuery, callback_data: CatalogCB):
    await query.answer()
    await query.message.edit_text("Select position", reply_markup=items_kb(callback_data.cat_id))

def start_text(full_name: str) -> str:
    return (
        f"Hello, {html.bold(full_name)}!\n"
        "In this bot you can buy goods from a universe far, far away."
    )
