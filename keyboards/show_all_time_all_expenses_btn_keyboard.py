from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def all_time_all_expenses_menu():
    all_time_all_expenses_kb = InlineKeyboardMarkup()

    back_from_all_time_all_expenses_btn = InlineKeyboardButton(text='Назад', callback_data='back_from_all_time_all_expenses_btn')

    all_time_all_expenses_kb.add(back_from_all_time_all_expenses_btn)

    return all_time_all_expenses_kb
