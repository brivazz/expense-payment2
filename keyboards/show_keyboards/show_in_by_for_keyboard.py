from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def show_report_in_by_for_menu():
    show_all_category_kb = InlineKeyboardMarkup(row_width=3)

    show_report_in_this_month_btn = InlineKeyboardButton(text='В этом месяце', callback_data='show_report_in_this_month_btn')
    show_report_by_months_btn = InlineKeyboardButton(text='По месяцам', callback_data='show_report_by_months_btn')
    show_report_for_the_year_btn = InlineKeyboardButton(text='За год', callback_data='show_report_for_the_year_btn')
    back_to_show_report_btn = InlineKeyboardButton(text='Назад', callback_data='back_to_show_report_btn')

    show_all_category_kb.add(show_report_in_this_month_btn, show_report_for_the_year_btn, show_report_by_months_btn)
    show_all_category_kb.add(back_to_show_report_btn)

    return show_all_category_kb
