from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def show_report_btn_menu():
    show_report_menu = InlineKeyboardMarkup(row_width=3)

    products_btn = InlineKeyboardButton(text='Продукты', callback_data='show_report_products_btn')
    tabak_btn = InlineKeyboardButton(text='Табак', callback_data='show_report_tabak_btn')
    alcohol_btn = InlineKeyboardButton(text='Алкоголь', callback_data='show_report_alcohol_btn')
    clothing_and_shoes = InlineKeyboardButton(text='Одежда и обувь', callback_data='show_report_clothing_and_shoes')
    mob_tel_btn = InlineKeyboardButton(text='Моб.связь', callback_data='show_report_mob_tel_btn')
    travel_btn = InlineKeyboardButton(text='Проезд', callback_data='show_report_travel_btn')
    rent_commun_payments_btn = InlineKeyboardButton(text='Аренда и ком.платежи', callback_data='show_report_rent_commun_payments_btn')
    leisure_btn = InlineKeyboardButton(text='Досуг', callback_data='show_report_leisure_btn')
    kindergarten_btn = InlineKeyboardButton(text='Детский сад', callback_data='show_report_kindergarten_btn')
    other_payments_btn = InlineKeyboardButton(text='Другие расходы', callback_data='show_report_other_payments_btn')
    my_zp_btn = InlineKeyboardButton(text='Моя ЗП', callback_data='show_report_my_zp_btn')
    my_love_zp_btn = InlineKeyboardButton(text='Любимая ЗП', callback_data='show_report_my_love_zp_btn')
    parents_btn = InlineKeyboardButton(text='Родители', callback_data='show_report_parents_btn')
    all_expense_month_btn = InlineKeyboardButton(text='Общие за месяц', callback_data='all_expense_month_btn')
    all_time_all_expenses_btn = InlineKeyboardButton(text='Общие за все время', callback_data='all_time_all_expenses_btn')
    back_from_show_report_menu_btn = InlineKeyboardButton(text='Назад', callback_data='back_from_show_report_menu_btn')

    show_report_menu.add(products_btn, tabak_btn, alcohol_btn)
    show_report_menu.add(clothing_and_shoes, kindergarten_btn)
    show_report_menu.add(travel_btn, mob_tel_btn, leisure_btn)
    show_report_menu.add(rent_commun_payments_btn, other_payments_btn)
    show_report_menu.add(my_zp_btn, parents_btn, my_love_zp_btn)
    show_report_menu.add(all_expense_month_btn, all_time_all_expenses_btn)
    show_report_menu.add(back_from_show_report_menu_btn)

    return show_report_menu
