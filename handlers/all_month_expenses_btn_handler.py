from aiogram.types import CallbackQuery

from utils.create_bot import dp, bot
from messages.all_month_expenses_btn_message import all_expenses_month_msg
from messages. show_report_btn_message import show_report_btn_msg
from keyboards.show_all_month_expenses_btn_keyboard import all_month_expenses_menu
from keyboards.show_report_btn_keyboard import show_report_btn_menu


@dp.callback_query_handler(text='all_month_expenses_btn')
async def all_expenses_month(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=await all_expenses_month_msg(),
        reply_markup=await all_month_expenses_menu()
    )


@dp.callback_query_handler(text='back_from_all_month_expenses_btn')
async def back_from_all_expenses_month(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=await show_report_btn_msg(),
        reply_markup=await show_report_btn_menu()
    )
