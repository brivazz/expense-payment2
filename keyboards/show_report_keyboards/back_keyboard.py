from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def back_menu():
    back_kb = InlineKeyboardMarkup()

    back_btn = InlineKeyboardButton(text='Назад', callback_data='back_from_in_by_for_btn')

    back_kb.add(back_btn)

    return back_kb
