from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def show_report_all_expenses_btn_menu(data):
    show_expenses_kb = InlineKeyboardMarkup()
    if data == 'show_all_month_expenses_btn':
        back_from_expenses_btn = InlineKeyboardButton(text='Назад', callback_data='back_from_show_all_month_expenses_btn')
    elif data == 'show_all_time_all_expenses_btn':
        back_from_expenses_btn = InlineKeyboardButton(text='Назад', callback_data='back_from_show_all_time_all_expenses_btn')

    show_expenses_kb.add(back_from_expenses_btn)

    return show_expenses_kb
