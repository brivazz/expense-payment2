from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


async def start_menu_kb():
    start_menu = InlineKeyboardMarkup(row_width=3)

    products_btn = InlineKeyboardButton(text='Продукты', callback_data='products_btn')
    tabak_btn = InlineKeyboardButton(text='Табак', callback_data='tabak_btn')
    alcohol_btn = InlineKeyboardButton(text='Алкоголь', callback_data='alcohol_btn')
    clothing_and_shoes = InlineKeyboardButton(text='Одежда и обувь', callback_data='clothing_and_shoes')
    mob_tel_btn = InlineKeyboardButton(text='Моб.связь', callback_data='mob_tel_btn')
    travel_btn = InlineKeyboardButton(text='Проезд', callback_data='travel_btn')
    rent_commun_payments_btn = InlineKeyboardButton(text='Аренда и ком.платежи', callback_data='rent_commun_payments_btn')
    leisure_btn = InlineKeyboardButton(text='Досуг', callback_data='leisure_btn')
    kindergarten_btn = InlineKeyboardButton(text='Детский сад', callback_data='kindergarten_btn')
    other_payments_btn = InlineKeyboardButton(text='Другие расходы', callback_data='other_payments_btn')
    my_zp_btn = InlineKeyboardButton(text='Моя ЗП', callback_data='my_zp_btn')
    my_love_zp_btn = InlineKeyboardButton(text='Любимая ЗП', callback_data='my_love_zp_btn')
    parents_btn = InlineKeyboardButton(text='Родители', callback_data='parents_btn')
    show_report_btn = InlineKeyboardButton(text='Показать записи', callback_data='show_report_btn')

    start_menu.add(products_btn, tabak_btn, alcohol_btn)
    start_menu.add(clothing_and_shoes, kindergarten_btn)
    start_menu.add(travel_btn, mob_tel_btn, leisure_btn)
    start_menu.add(rent_commun_payments_btn, other_payments_btn)
    start_menu.add(my_zp_btn, parents_btn, my_love_zp_btn)
    start_menu.add(show_report_btn)

    return start_menu
