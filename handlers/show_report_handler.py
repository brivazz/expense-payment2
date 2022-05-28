from aiogram.types import CallbackQuery

from utils.create_bot import dp, bot
from messages.show_report_btn_message import show_report_btn_msg
from messages.start_message import start_msg
from keyboards.show_report_btn_keyboard import show_report_btn_menu
from keyboards.start_keyboard import start_menu_kb


@dp.callback_query_handler(text='show_report_btn')
async def show_report(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=await show_report_btn_msg(),
        reply_markup=await show_report_btn_menu()
    )


@dp.callback_query_handler(text='back_from_show_report_menu_btn')
async def back_from_show_report(call: CallbackQuery):
    await call.answer()
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=call.message.message_id,
        text=await start_msg(call.from_user.full_name),
        reply_markup=await start_menu_kb()
    )
