from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def all_month_expenses_menu():
    all_month_expenses_kb = InlineKeyboardMarkup()

    back_from_all_month_expenses_btn = InlineKeyboardButton(text='Назад', callback_data='back_from_all_month_expenses_btn')

    all_month_expenses_kb.add(back_from_all_month_expenses_btn)

    return all_month_expenses_kb
