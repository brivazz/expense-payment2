from aiogram.types import CallbackQuery
from aiogram.utils.exceptions import MessageNotModified

from utils.create_bot import dp, bot
from messages.start_message import start_msg
from messages.show_messages.show_category_message import show_category_msg
from messages.show_messages.show_report_in_by_for_btn_message import show_report_in_by_for_btn_msg
from messages.show_messages.show_all_expenses_btn_message import all_expenses_btn_msg

from keyboards.start_keyboard import start_menu_kb
from keyboards.show_keyboards.show_in_by_for_keyboard import show_report_in_by_for_menu
from keyboards.show_keyboards.back_keyboard import back_menu
from keyboards.show_keyboards.show_all_expenses_btn_keyboard import show_all_expenses_btn_menu
from keyboards.show_keyboards.show_report_btn_keyboard import show_report_btn_menu


@dp.callback_query_handler(text='back_from_show_report_menu_btn')
async def back_from_show_report(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=await start_msg(call.from_user.full_name),
        reply_markup=await start_menu_kb()
    )


@dp.callback_query_handler(text=['show_report_products_btn',
                                 'show_report_tabak_btn',
                                 'show_report_alcohol_btn',
                                 'show_report_clothing_and_shoes',
                                 'show_report_mob_tel_btn',
                                 'show_report_travel_btn',
                                 'show_report_rent_commun_payments_btn',
                                 'show_report_leisure_btn',
                                 'show_report_kindergarten_btn',
                                 'show_report_other_payments_btn',
                                 'show_report_my_zp_btn',
                                 'show_report_parents_btn',
                                 'show_report_my_love_zp_btn',
                                 'back_from_in_by_for_btn'])
async def show_report_buttons(call: CallbackQuery):
    await call.answer()
    if call.data == 'show_report_products_btn':
        category_text = 'Продукты'
    elif call.data == 'show_report_tabak_btn':
        category_text = 'Табак'
    elif call.data == 'show_report_alcohol_btn':
        category_text = 'Алкоголь'
    elif call.data == 'show_report_clothing_and_shoes':
        category_text = 'Одежда и обувь'
    elif call.data == 'show_report_mob_tel_btn':
        category_text = 'Моб.связь'
    elif call.data == 'show_report_travel_btn':
        category_text = 'Проезд'
    elif call.data == 'show_report_rent_commun_payments_btn':
        category_text = 'Аренда и ком.платежи'
    elif call.data == 'show_report_leisure_btn':
        category_text = 'Досуг'
    elif call.data == 'show_report_kindergarten_btn':
        category_text = 'Детский сад'
    elif call.data == 'show_report_other_payments_btn':
        category_text = 'Другие расходы'
    elif call.data == 'show_report_my_zp_btn':
        category_text = 'Моя ЗП'
    elif call.data == 'show_report_parents_btn':
        category_text = 'Родители'
    elif call.data == 'show_report_my_love_zp_btn':
        category_text = 'Любимой ЗП'
    elif call.data == 'back_from_in_by_for_btn':
        category_text = call.message.text.split('==')[1]
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=await show_category_msg(category_text),
        reply_markup=await show_report_in_by_for_menu()
    )


@dp.callback_query_handler(text=['show_report_in_this_month_btn',
                                 'show_report_by_months_btn',
                                 'show_report_for_the_year_btn'])
async def show_report_in_by_for(call: CallbackQuery):
    await call.answer()
    print(call.message.text)
    try:
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=call.message.message_id,
            text=await show_report_in_by_for_btn_msg(call.data, call.message.text),
            reply_markup=await back_menu()
        )
    except MessageNotModified:
        pass



@dp.callback_query_handler(text=['show_all_month_expenses_btn',
                                 'show_all_time_all_expenses_btn'])
async def show_report_all_time_all_month(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=await all_expenses_btn_msg(call.data),
        reply_markup=await show_all_expenses_btn_menu(call.data)
    )


@dp.callback_query_handler(text=['show_report_btn',
                                 'back_from_show_all_time_all_expenses_btn',
                                 'back_from_show_all_month_expenses_btn',
                                 'back_to_show_report_btn'])
async def back_from_all_time_all_month(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text='Показать записи:',
        reply_markup=await show_report_btn_menu()
    )
