from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def save_menu():
    save_products_kb = InlineKeyboardMarkup()

    save_btn = InlineKeyboardButton(text='Сохранить', callback_data='save_btn')
    cancel_btn = InlineKeyboardButton(text='Отменить', callback_data='cancel_btn')

    save_products_kb.add(save_btn)
    save_products_kb.add(cancel_btn)

    return save_products_kb
